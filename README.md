# SAM File Searcher

Script and functions for parsing and searching SAM files.

## Options

* `-i, --input-file` Input file to read
* `-s, --sequence` Sequence to search for
* `-t, --type` Type of match to look for

Run the command without any arguments to print the help.

### Match Types

* `leading` Looks for the search sequence at the start of the string
* `trailing` Looks for the search sequence at the end of the string
* `midway` Looks for the search sequence at either the start of the string or offset by one from the start

## Examples

```shell
$> ./bin/extract-counts -i data/toy.sam -s tta
TTA is a leading match in TTAGATAAAGAGGATACTG
TTA is a leading match in TTATAAAACAAATAATTAAGTCTACA

$> ./bin/extract-counts -i data/toy.sam -s tta
TTA is a leading match in TTAGATAAAGAGGATACTG
TTA is a leading match in TTATAAAACAAATAATTAAGTCTACA

$> ./bin/extract-counts -i data/toy.sam -s aaa -t trailing
AAA is a trailing match in AAAAGATAAGGGATAAA

$> ./bin/extract-counts -i data/toy.sam -s agc -t trailing
AGC is a trailing match in ATAGCTCTCAGC

$> ./bin/extract-counts -i data/toy.sam -s agc -t midway
AGC is a midway match in AGCTAA
AGC is a midway match in CAGCGCCAT
```
