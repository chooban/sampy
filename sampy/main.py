import sys

from lib import Options
from lib import SamSearcher

def print_match_counts(searcher, match_type):
    if match_type == 'leading':
        print "Found", searcher.count_leading(), "matches"
    elif match_type == 'trailing':
        print "Found", searcher.count_trailing(), "matches"
    elif match_type == 'midway':
        print "Found", searcher.count_midway(), "matches"

def print_matches(search, match_type):
    if match_type == 'leading':
        print "Found", searcher.leading_matches()
    elif match_type == 'trailing':
        print "Found", searcher.trailing_matches()
    elif match_type == 'midway':
        print "Found", searcher.midway_matches()

if __name__ == '__main__':
    options = Options()

    if len(sys.argv[1:]) == 0:
        options.help()
        sys.exit(0)

    opts = options.parse(sys.argv[1:])

    if opts.input_file == None:
        print("Please supply an input file")
        sys.exit(1)

    try:
        searcher = SamSearcher(opts.input_file, opts.sequence)
    except:
        print sys.exc_info()
        sys.exit(1)

    if opts.count:
        print_match_counts(searcher, opts.type)
    else:
        print_matches(searcher, opts.type)

    sys.exit(0)
