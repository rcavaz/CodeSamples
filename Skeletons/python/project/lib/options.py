#!/usr/bin/env python
from argparse import ArgumentParser


class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage = 'bin/project'
        self.parser = ArgumentParser(usage=usage)
        self.parser.add_argument('-n'
                                ,'--name'
                                ,default='World'
                                ,dest='name'
                                ,help='Who to greet')
        self.parser.add_argument('-d'
                                ,'--debug'
                                ,action="store_true"
                                ,help='Switch on to debug mode')
        self.parser.add_argument('-v'
                                ,'--verbose'
                                ,action="store_true"
                                ,help='Switch on to verbose mode')

    def parse(self, args=None):
        self.known, self.unknown = self.parser.parse_known_args(args)[:]
        if len(self.unknown) != 0:
            print '[WARN] Unknown args received: '+repr(self.unknown)
