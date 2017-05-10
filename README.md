# SAM File Searcher

Script and functions for parsing and searching SAM files.

## Options

* `-s, --sequence` Sequence to search for
* `-t, --type` Type of match to look for
* `-c` Print counts

Run the command without any arguments to print the help.

### Match Types

* `leading` Looks for the search sequence at the start of the string
* `trailing` Looks for the search sequence at the end of the string
* `midway` Looks for the search sequence at either the start of the string or offset by one from the start

## Examples

```shell
$> ./bin/extract-counts -s tta -c data/toy.sam
Found 2 matches for tta

$> ./bin/extract-counts -s tta -c data/*.sam
Found 4 matches for tta
```
