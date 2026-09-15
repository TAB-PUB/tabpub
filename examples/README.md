# Reuse examples

Requirements: Python 3.10 or newer. No additional Python packages or network access are needed.

Run these commands from the repository root:

```sh
python3 examples/group_memberships.py examples/synthetic/research.json
python3 examples/secondary_relations.py examples/synthetic/research.json
python3 -m unittest discover -s tests -v
```

The first command lists group membership and preserves the distinction between full and partial agreement. The second produces a directed edge list from secondary groups to their recorded targets. It does not infer relationships from matching text or from alphabetical group labels.

To analyze an unpacked publication dataset, replace the input argument with its directory. The scripts recognize a verse package's data/research.json and a chapter package's verses/*/data/research.json. They support the tabpub-scholarly-collation-1 research format used by the production 4.0 export.

The examples read only the scholarly research records. They do not parse the package's JSON-LD graph, verify its licenses or validate its complete schema. Their checks cover the group references needed for these two analyses.

## Synthetic data

DEMO.1.1 is not a biblical reference. All memberships and assessments in the fixture are invented for demonstration. The fixture contains no source-edition text, no actual research decisions, no approval provenance and no dataset DOI. Its quotation identifiers are illustrative placeholders; it is a research-record fragment, not a complete publication package.

- Unit 1 illustrates complete agreement without assigning a primary judgment.
- Unit 2 illustrates M assessed as secondary to a primary group and S partially agreeing with that group.
- Unit 3 illustrates a secondary group related to two literary groups.

A group is identified within its context and unit. Do not combine identically named groups from different units as though they were one entity.

When reporting an analysis of real data, record the dataset's version DOI and the version or commit of the script used. Preserve the source and licensing information in the original package.
