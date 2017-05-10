import sys

from lib import Options
from lib import SamSearcher

if __name__ == '__main__':
    options = Options()

    if len(sys.argv[1:]) == 0:
        options.help()
        sys.exit(0)

    opts = options.parse(sys.argv[1:])

    if opts.input_files == None:
        print("Please supply an input file or glob")
        sys.exit(1)

    if opts.input_files.__len__() == 0:
        print("Could not find any matching input files")
        sys.exit(1)

    if opts.count:
        count = 0
        for infile in opts.input_files:
            searcher = SamSearcher(infile, opts.sequence, opts.type)
            count += searcher.count()
        print "Found", count, "matches for", opts.sequence
    else:
        matches = []
        for infile in opts.input_files:
            searcher = SamSearcher(infile, opts.sequence, opts.type)
            matches.append(searcher.matches())
        print "Found", matches

    sys.exit(0)
