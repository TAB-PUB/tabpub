# Contributing

This page is for readers, researchers and developers who would like to report a problem or propose a correction to the public documentation and examples.

## Questions and corrections

[Repository issues](https://github.com/TAB-PUB/tabpub/issues) are suitable for documentation questions and reproducible problems with the example scripts. A useful report identifies the relevant file or version, describes the problem and, where applicable, includes a small example and the expected result.

Questions about a published dataset are easier to investigate when they include its version DOI and the passage or unit concerned. Substantial methodological proposals benefit from discussion before a pull request. Changes to this repository do not directly alter the Approved collations in the research application.

Issues and pull requests are public. Reports should contain only material suitable for public distribution; confidential records, credentials and restricted source material belong outside these discussions. A synthetic example is usually sufficient to illustrate a software problem.

## Proposed changes

Documentation and synthetic-data contributions use CC BY 4.0; contributions to the independent Python examples and tests use MIT. Contributors need the authority to submit their material under the relevant license. Third-party attribution and license notices remain applicable.

Changes to the Python examples can be checked from the repository root with:



```sh
python3 -m unittest discover -s tests -v
```

A scholarly correction should identify its evidence and distinguish a proposed interpretation from an error in the published record.
