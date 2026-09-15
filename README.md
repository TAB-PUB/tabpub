<img src="TAB-PUB_logo.png" alt="TAB-PUB logo" width="140">

# TAB-PUB

**Tracking Ancient Bible Publishers: Variant Editions Behind the Hebrew Bible**

TAB-PUB investigates textual variation and literary editions behind the Hebrew Bible. Its digital research environment connects witness verification, correspondence mapping, collation and scholarly assessment. The current application supports work on 1 and 2 Kings.

[Project website](https://tabpub.elte.hu/) · [Textual Collations](https://tabpub.elte.hu/collation/results.php) · [Datasets on Zenodo](https://zenodo.org/communities/tab-pub)

## About this repository

This repository documents the research workflow, the interpretation of the exported data and the distinction between source readings and scholarly decisions. It is a documentation repository, not a distribution of the hosted editing application.

- [Research workflow](docs/workflow.md)
- [Data and interpretation](docs/data-model.md)
- [Using and citing the outputs](docs/reuse.md)
- [Sources and rights](docs/sources-and-rights.md)
- [Run the examples](examples/README.md)
- [Maintenance and releases](docs/maintenance.md)

## Research outputs

**Textual Collations** presents the current Approved collations. This is a changing view: a newly approved or revised passage can change what is displayed.

**Publication datasets** are versioned exports intended for repository deposit. A verse dataset records the approved reading groups, assessments, relationships, reconstructions and source references. Chapter datasets combine the approved verses in the selected text mode. JSON supplies the records; JSON-LD represents their data and relationships as a graph.

The public reader and an archived dataset serve different purposes. Cite a deposited dataset version when reporting an analysis of a fixed body of data. Dataset deposits are collected in the [TAB-PUB Zenodo community](https://zenodo.org/communities/tab-pub). Use the DOI of the individual record and version when citing data; the community URL is a collection address, not a dataset DOI.

## Scope and interpretation

Agreement groups express a researcher's assessment of textual agreement across witnesses. They do not require identical strings across languages. Partial agreement, omission, uncertain assessment and Hebrew reconstruction are represented separately. An Approved collation records a completed editorial decision within the project; it does not imply that the interpretation is beyond revision.

See the documentation before comparing group labels or interpreting reconstructed readings.

## Project and funding

Host: Institute of Ancient Studies, Faculty of Humanities, Eötvös Loránd University (ELTE BTK Ókortudományi Intézet).

NKFIH STARTING_25, grant 152433.

Authorship of individual datasets is recorded in their release metadata. Dataset authorship and maintenance of this documentation are distinct roles.

## Licensing

Original documentation and synthetic teaching data are available under [CC BY 4.0](LICENSE.md). Example Python scripts and tests use the MIT license. The hosted application and third-party source editions are not licensed by this repository. Dataset licenses and source-specific rights are stated in each deposited package.
