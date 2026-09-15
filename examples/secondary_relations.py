# SPDX-License-Identifier: MIT
"""Output a CSV edge list of explicitly recorded secondary relationships."""
import argparse
import csv
import sys
from read_dataset import documents, relationships


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='research.json or unpacked publication directory')
    args = parser.parse_args()
    rows = [row for data in documents(args.input) for row in relationships(data)]
    writer = csv.writer(sys.stdout)
    writer.writerow(['context', 'unit', 'secondary_group_id', 'target_group_id', 'characterization'])
    writer.writerows(rows)


if __name__ == '__main__':
    main()
