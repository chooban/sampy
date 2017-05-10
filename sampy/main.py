import sys
import os

from lib import Options
from lib import Sam

if __name__ == '__main__':
    options = Options()
    opts = options.parse(sys.argv[1:])

    if opts.input_file == None:
        print("Please supply an input file")
        sys.exit(1)

    if not os.path.isfile(opts.input_file):
        print("Could not find specified file")
        sys.exit(1)

    sam_file = open(opts.input_file, 'r')

    subseq = opts.sequence.upper()
    sam = Sam()
    for line in sam_file.readlines():
        seq = sam.extract_sequence(line)
        if seq == None:
            continue

        if opts.type == 'leading':
            match = sam.is_leading_match(seq, subseq)
            if match:
                print subseq + ' is a leading match in ' + seq
        elif opts.type == 'trailing':
            match = sam.is_trailing_match(seq, subseq)
            if match:
                print subseq + ' is a trailing match in ' + seq
        elif opts.type == 'midway':
            match = sam.is_midway_match(seq, subseq)
            if match:
                print subseq + ' is a midway match in ' + seq
