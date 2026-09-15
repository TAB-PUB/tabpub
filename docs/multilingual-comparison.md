# Multilingual comparison

TAB-PUB compares witness readings across Hebrew, Greek, Latin, Syriac and Aramaic. The essential distinction is between **correspondence**, which establishes comparable textual spans, and **agreement**, which evaluates their textual relationship.

## From witness text to aligned units

1. **Witness preparation.** Researchers verify electronic starting texts against the relevant facsimile or edition. Workbench records preserve corrections, local variants, source references and textual states.
2. **Correspondence.** Researchers select source-token references for each side of a correspondence group. A side can contain several tokens: cross-language correspondence does not require a one-word-to-one-word mapping. Selected local variants retain links to the groups in which they occur.
3. **Core input.** A server-side adapter converts the verified groups into Core apparatus units. Positions are anchored to the M-L token sequence; groups without M-L tokens receive intervening positions. Witness language, script, direction and source references are carried into the input. These positions are alignment coordinates, not an assertion that M preserves the primary reading.
4. **Editorial units.** In Set Variants, researchers can combine adjacent units using Core's unit-editing interaction. The subsequent assessment uses the current edited unit and its readings.

This pathway constructs a prealigned apparatus. It does not ask a string-matching engine to infer equivalence between languages. Missing verified correspondence requires further research preparation rather than an automatic alignment fallback.

## Correspondence is not agreement

Two expressions may refer to the same part of a verse while representing different readings. Conversely, different languages necessarily have different word forms even when the researcher judges their readings to agree.

For example, an invented unit could contain M in group **a**, G and S in group **b**, and V in group **c**. If S supports the same reading as G but has a meaningful additional suffix, the researcher may record S as a partial member of b, displayed as **(S)**. Neither membership nor partial agreement is inferred automatically from the strings. The synthetic records in [the examples](../examples/README.md) illustrate this distinction without reproducing source-edition text.

The assessment interface uses M as the initial comparison baseline. Readings that agree with M join a; differing readings can be placed together in other groups. Group a can itself be assessed as secondary. Primary, secondary, literary and uncertain are research judgments, not similarity scores.

## Text form and absence

Edition text and comparison text have distinct roles. Witness-specific policies control features such as punctuation and diacritics while retaining source provenance. Normalization facilitates presentation and comparison; it does not establish semantic agreement or replace the edition record. Language direction affects display, not the identity of a correspondence group.

An explicit omission differs from a passage that is not preserved or not applicable to a witness. Empty text alone is insufficient evidence for omission. Local variants and their sources are scoped to their attestations, rather than being treated as continuous new witnesses throughout the book.

## Reconstruction and limits

Preferred Hebrew readings and literary retroversions are researcher-entered proposals. They are separate from attested source texts and notes, and appear in angle brackets. They are not automatic translations of Greek, Latin or Syriac readings.

The software records and checks the consistency of editorial decisions. It does not decide whether a reading is primary, diagnose its secondary cause, or independently validate a proposed Hebrew reconstruction. The interpretive responsibility remains with the researchers.
