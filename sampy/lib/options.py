import glob

from argparse import ArgumentParser

class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage = 'bin/extract-counts'
        self.parser = ArgumentParser(usage=usage)
        self.parser.add_argument('input_files',
                                 nargs='*',
                                 help='Input file(s) to read')
        self.parser.add_argument('-s',
                                 '--sequence',
                                 required=True,
                                 dest='sequence',
                                 help='Sequence to search for')
        self.parser.add_argument('-t',
                                 '--type',
                                 default='leading',
                                 dest='type',
                                 help='Type of match')
        self.parser.add_argument('-c',
                                '--count',
                                default=False,
                                action='store_true',
                                help='Print counts instead of matches')

    def parse(self, args=None):
        return self.parser.parse_args(args)

    def help(self):
        self.parser.print_help()
