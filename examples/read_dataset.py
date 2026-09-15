# SPDX-License-Identifier: MIT
"""Read TAB-PUB scholarly research JSON from a file or unpacked publication."""
import json
from pathlib import Path


def documents(path):
    path = Path(path)
    if path.is_file():
        files = [path]
    elif (path / 'data/research.json').is_file():
        files = [path / 'data/research.json']
    else:
        files = sorted(path.glob('verses/*/data/research.json'))
    if not files:
        raise ValueError('No scholarly research JSON found.')
    for file in files:
        data = json.loads(file.read_text(encoding='utf-8'))
        if data.get('schema') != 'tabpub-scholarly-collation-1':
            raise ValueError(f'Unsupported research schema: {file}')
        units_seen = set()
        for unit in data['units']:
            uid = unit['unit_id']
            if uid in units_seen:
                raise ValueError(f'Duplicate unit: {uid}')
            units_seen.add(uid)
            groups = unit['groups']
            order = unit['order']
            if len(set(order)) != len(order) or set(order) != set(groups):
                raise ValueError(f'Group order does not match groups in {uid}')
            for reading in unit['readings']:
                if reading['group'] not in groups:
                    raise ValueError(f'Unknown reading group in {uid}')
                if not isinstance(reading.get('partial'), bool):
                    raise ValueError(f'Invalid partial membership in {uid}')
            for gid, group in groups.items():
                for target in group.get('secondary_to_groups', []):
                    if target not in groups or target == gid:
                        raise ValueError(f'Invalid secondary relationship in {uid}')
        yield data


def memberships(data):
    for unit in data['units']:
        for gid in unit['order']:
            for reading in unit['readings']:
                if reading['group'] == gid:
                    yield (data['context'], unit['unit_id'], gid,
                           unit['groups'][gid].get('judgment', ''),
                           reading['witness'], reading['id'],
                           'partial' if reading['partial'] else 'full')


def relationships(data):
    for unit in data['units']:
        for gid in unit['order']:
            group = unit['groups'][gid]
            if group.get('judgment') == 'secondary':
                for target in group.get('secondary_to_groups', []):
                    yield (data['context'], unit['unit_id'], gid, target,
                           group.get('characterization', ''))
