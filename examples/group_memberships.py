# SPDX-License-Identifier: MIT
"""Output one CSV row per reading, preserving partial agreement."""
import argparse
import csv
import sys
from read_dataset import documents, memberships


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='research.json or unpacked publication directory')
    args = parser.parse_args()
    rows = [row for data in documents(args.input) for row in memberships(data)]
    writer = csv.writer(sys.stdout)
    writer.writerow(['context', 'unit', 'group_id', 'judgment', 'witness', 'reading_id', 'membership'])
    writer.writerows(rows)


if __name__ == '__main__':
    main()
