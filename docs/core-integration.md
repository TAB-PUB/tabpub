# Core integration and modifications

Collation Editor Core is designed to be embedded in a larger application through a services layer. TAB-PUB uses that extension point to supply researcher-defined multilingual alignment. This is a change in how the apparatus is prepared and assessed, rather than a claim that Core itself performs semantic comparison across languages.

## Integration layers

| Layer | TAB-PUB implementation | Effect |
| --- | --- | --- |
| Input adapter | `preparation-core-model.php` | Converts verified Correspondence groups and source-token references into a prealigned Core apparatus; retains local attestations and source snapshots. |
| Application services | `tabpub_services.js` | Connects Core to passage preparation, saved revisions and project storage. The active mapped route uses the preparation API rather than automatic string alignment. |
| Native data adaptation | `core-assessment-model.js` | Prepares token structures for native Core editing, retaining input fields in project metadata; defines group memberships and assessment records. |
| Assessment interface | `core-assessment.js` | Extends Core rendering and save interactions; provides group assignment, partial agreement, characterization and reconstruction in Order Readings. |
| Server validation | `core-assessment-model.php` and `save.php` | Validates the assessment against its recorded unit basis and checks completeness for approval. |
| Publication | Public-results and export modules | Derives the reader and dataset projection from saved Approved records, with sources and provenance. |

These filenames identify components of the hosted application; they are not links to source files distributed by this documentation repository.

## Direct edits in Core files

The deployed 4.0 release payload contains three directly adapted Core JavaScript files. A comparison with upstream commit `58f41b24174eddfcaf5c738bfc07243182c3a895` identifies the following differences. This comparison reference is not asserted to be the historical commit from which the installation was originally obtained.

| Core file | Direct adaptation |
| --- | --- |
| `collation.js` | Calls the project `onIndexReady` service after the passage form is ready; stops initialization when witness selection returns an invalid or empty list. |
| `set_variants.js` | Calls the optional TAB-PUB Masoretic reading-display decorator. |
| `order_readings.js` | Calls the same display decorator while retaining the undecorated stored reading string. |

The larger change is in the surrounding services and runtime extensions described above. In the supplied earlier TAB-PUB snapshot, a custom renderer returned early from Core's unit-rendering functions. Those early returns were removed in the 4.0 payload so native unit editing could operate. The later assessment extension presents readings grouped by scholarly decisions in Order Readings and Approved views.

## Differences from a conventional automatic collation workflow

- **Alignment:** verified token correspondences determine the initial apparatus; matching spellings across languages do not.
- **Regularisation:** the mapped route supplies no Core regularisation rules and prevents rule editing there. Source adjustments belong in the Workbenches and alignment changes in Correspondence. Legacy regularisation/settings controls are hidden on this route.
- **Recollation:** the mapped interface labels this action **Reload Correspondence**. It reloads verified upstream alignment and can replace current Core edits; saved Core revisions are the basis for continued editorial work.
- **Unit editing:** Set Variants retains native unit combination. Assessment is deferred until Order Readings, after unit boundaries have been established.
- **Reading groups:** scholarly groups can span languages, record partial membership, and distinguish their ordering from judgments of textual priority.
- **Persistence:** assessments are saved with Core and carry the unit basis they assess. A changed basis requires review rather than silent reuse of an earlier judgment.

## Scope of the evidence

This description was checked against the local source snapshot and the 4.0/4.0.1 deployment payloads. Version 4.0.1 adds software attribution to exports; it does not change alignment or grouping. The exact historical upstream revision and complete corresponding-source provision remain open items in the [software licensing record](software-attribution.md). The table is a documented comparison, not a complete distribution manifest for every library in the hosted service.
