#!/usr/bin/env python
import sys


from lib import Options
from lib import Project


def run(args):
    opts = Options()
    opts.parse(args[1:])

    w = Project(opts)
    print w.welcome()


if __name__ == '__main__':
    run(sys.argv)
