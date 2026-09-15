# SPDX-License-Identifier: MIT
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'examples'))
from read_dataset import documents, memberships, relationships


class Examples(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'examples/synthetic/research.json').read_text())

    def test_semantics(self):
        rows = list(memberships(self.data))
        self.assertEqual(len(rows), 11)
        self.assertEqual([r[4] for r in rows if r[-1] == 'partial'], ['S'])
        edges = list(relationships(self.data))
        self.assertEqual([(r[1], r[2], r[3]) for r in edges], [
            ('demo-u2', 'g-m', 'g-b'),
            ('demo-u3', 'g-c', 'g-m'), ('demo-u3', 'g-c', 'g-b')])
        self.assertTrue(all(r[3] == '' for r in rows if r[1] == 'demo-u1'))

    def test_verse_and_chapter(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            verse = root / 'verse/data/research.json'
            verse.parent.mkdir(parents=True)
            verse.write_text(json.dumps(self.data))
            self.assertEqual(len(list(documents(root / 'verse'))), 1)
            for context in ['DEMO.1.1', 'DEMO.1.2']:
                target = root / 'chapter/verses' / context / 'data/research.json'
                target.parent.mkdir(parents=True)
                data = copy.deepcopy(self.data)
                data['context'] = context
                target.write_text(json.dumps(data))
            loaded = list(documents(root / 'chapter'))
            self.assertEqual([d['context'] for d in loaded], ['DEMO.1.1', 'DEMO.1.2'])

    def test_invalid_group_and_schema(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'research.json'
            for mutation in ['target', 'schema', 'partial']:
                data = copy.deepcopy(self.data)
                if mutation == 'target':
                    data['units'][1]['groups']['g-m']['secondary_to_groups'] = ['absent']
                elif mutation == 'schema':
                    data['schema'] = 'unknown'
                else:
                    data['units'][0]['readings'][0]['partial'] = 'false'
                target.write_text(json.dumps(data))
                with self.assertRaises(ValueError):
                    list(documents(target))


if __name__ == '__main__':
    unittest.main()
