# DNA Playground

## Usage
* `make build`
* `make start`
* `make run pipeline=covid`
* `make stop`

## Resources
* Biopython: [website](https://biopython.org), [tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html)
* Nextstrain: [website](https://nextstrain.org), [github](https://github.com/nextstrain)

## Data Sources
* Nextstrain COVID-19 analysis: [github](https://github.com/nextstrain/ncov), [sequences.fasta](https://raw.githubusercontent.com/nextstrain/ncov/master/example_data/sequences.fasta), [metadata.tsv](https://raw.githubusercontent.com/nextstrain/ncov/master/data/metadata.tsv)

## TODO
* Refine phylo tree prior to plotting using augur + metadata: https://github.com/nextstrain/ncov/blob/master/Snakefile#L245-L260
* Build ancestral tree using augur https://github.com/nextstrain/ncov/blob/master/Snakefile#L278-L283
* Add pytest, yapf
