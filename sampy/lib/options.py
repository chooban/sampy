from argparse import ArgumentParser

class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage = 'bin/extract-counts'
        self.parser = ArgumentParser(usage=usage)
        self.parser.add_argument('-i',
                                 '--input-file',
                                 dest='input_file',
                                 help='Input file to read')
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

    def parse(self, args=None):
        return self.parser.parse_args(args)
