<img src="TAB-PUB_logo.png" alt="TAB-PUB logo" width="140">

# TAB-PUB

**Tracking Ancient Bible Publishers: Variant Editions Behind the Hebrew Bible**

TAB-PUB studies textual variation and literary editions of the Hebrew Bible through comparison of Hebrew witnesses and ancient translations. Its research environment supports work on 1 and 2 Kings, connecting witness verification, correspondence mapping, collation and scholarly assessment.

[Project website](https://tabpub.elte.hu/) · [Textual Collations](https://tabpub.elte.hu/collation/results.php) · [Datasets on Zenodo](https://zenodo.org/communities/tab-pub)

## Preparing the evidence

In the [witness Workbenches](docs/workbenches.md), researchers verify source texts, record corrections and local variants, identify their sources and document preservation. Correspondence then selects and aligns this checked material. These preparation stages supply the evidence assessed in Core.

## Comparing texts across languages

Researchers identify corresponding passages in Hebrew, Greek, Latin, Syriac and Aramaic. TAB-PUB converts these verified correspondences into a prealigned apparatus for Collation Editor Core. Researchers then edit unit boundaries and assess which readings represent the same textual tradition, partially agree, or differ.

**Correspondence and agreement are separate decisions.** Placing two readings in the same unit makes them comparable; it does not declare them equivalent. The application does not infer cross-language agreement from spelling, machine translation or a semantic similarity score.

- [Multilingual comparison](docs/multilingual-comparison.md): alignment, textual states and scholarly grouping.
- [Research workflow](docs/workflow.md): from witness verification to an Approved collation.
- [Data and interpretation](docs/data-model.md): groups, assessments, reconstructions and exported records.

## Software foundation

TAB-PUB embeds and adapts [Collation Editor Core](https://github.com/itsee-birmingham/collation_editor_core), created by Catherine Smith at the Institute for Textual Scholarship and Electronic Editing (ITSEE), University of Birmingham. Catherine Smith and Troy A. Griffitts carried out the restructuring for release 1.0.

Core supplies the editorial stages and unit-editing interface. TAB-PUB supplies the correspondence-based input, project services, scholarly assessment, public reader and dataset exports. Most adaptations are implemented in the surrounding services and extension modules; the direct Core edits are documented separately.

- [Core integration and modifications](docs/core-integration.md)
- [Software attribution and licensing](docs/software-attribution.md)

## Research outputs and reuse

**Textual Collations** displays the current saved Approved material. Coverage and readings can change as research is approved or revised.

**Publication datasets** preserve a versioned scholarly projection: reading groups, assessments, relationships, reconstructions, quoted readings, source references and provenance. JSON supplies the records; JSON-LD represents their relationships as a graph. Chapter packages combine the Approved verses in the selected text mode.

Deposits are collected in the [TAB-PUB Zenodo community](https://zenodo.org/communities/tab-pub). Each deposit's version DOI identifies the fixed data used in an analysis; the community address identifies the collection.

- [Using and citing the outputs](docs/reuse.md)
- [Sources and rights](docs/sources-and-rights.md)
- [Executable examples and synthetic data](examples/README.md)
- [Maintenance and releases](docs/maintenance.md)

The examples demonstrate group membership and secondary relationships with invented records. They are not evidence for a biblical passage. This repository contains documentation and independent reuse examples; it is not a distribution of the complete hosted editing application.

## Project and funding

Host: Institute of Ancient Studies, Faculty of Humanities, Eötvös Loránd University (ELTE BTK Ókortudományi Intézet).

Funding: National Research, Development and Innovation Office (NKFIH), STARTING_25, grant 152433.

Creators and scholarly contributors are identified in each dataset's release metadata. Maintaining this repository does not imply authorship of every dataset.

## Licensing and contributions

Original documentation and synthetic teaching data: **CC BY 4.0**. Independent Python examples and tests: **MIT**. Collation Editor Core retains its **GNU GPL v3** license. Source editions and dataset quotations retain their separately documented rights. The project logo is excluded from the documentation and code licenses. Details are in [LICENSE.md](LICENSE.md).

[Contributing](CONTRIBUTING.md) explains how readers and developers can report problems or propose corrections.
