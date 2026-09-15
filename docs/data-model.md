# Data and interpretation

This is a conceptual guide. The vocabulary included with a particular dataset release documents its serialized fields and relationships.

| Entity | Meaning |
| --- | --- |
| Passage | A verse identified in the project catalogue. |
| Unit | A segment of the edited collation. Boundaries are editorial decisions. |
| Witness reading | The selected text or textual state attested by a witness within the unit. |
| Reading group | Readings assessed as belonging together in the unit, including qualified memberships. |
| Assessment | The researcher's characterization of a group. |
| Secondary relationship | A relationship between a secondary group and the group or groups to which it is related. |
| Reconstruction | A proposed Hebrew reading, distinct from a witness transcription. |
| Source reference | The edition or manuscript, locator and provenance associated with a reading. |
| Approved revision | The saved Core state underlying the publication projection. |

## Group labels

Labels such as a, b and c are local to a unit. Group a is anchored to M; that does not automatically make it primary. Group b in one unit is not the same entity as group b in another unit.

Partial agreement records a qualified membership in a group. It is not interchangeable with full agreement. The public interface uses parentheses to distinguish partial support.

## Assessments and reconstruction

Primary, secondary, literary and uncertain are scholarly assessments. A secondary explanation is researcher-entered text and should not be treated as a controlled taxonomy without further processing.

A preferred Hebrew reconstruction can accompany a primary group when M is assessed as secondary. Literary groups without an M reading can carry Hebrew retroversion. Reconstructions are displayed in angle brackets and remain distinct from notes and attested source texts.

## Files and graph

Verse publication packages separate research decisions, quoted readings, source references and provenance into JSON files. A JSON-LD graph represents the data and relationships. Chapter packages place verse records in separate directories and combine their graph representation.

Identifiers in an export identify records and revisions. They are not automatically repository DOIs. Preserve the package vocabulary, provenance and license files when reusing the data.
