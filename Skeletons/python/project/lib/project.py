#!/usr/bin/env python
import logging


class Project:

    def __init__(self, options):
        self.logger  = logging.getLogger('Project')
        self.options = options

        if self.options.known.verbose == True:
            self.logger.setLevel(logging.INFO)

        if self.options.known.debug == True:
            self.logger.setLevel(logging.DEBUG)

        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console.setFormatter(formatter)
        self.logger.addHandler(console)

    def welcome(self):
        self.logger.debug('This is a debug message')
        self.logger.info('This is an info message')
        self.logger.warning('This is a warning message')
        return "Hello, %s!" % self.options.known.name


# See more on logging:
# 1. https://docs.python.org/2/howto/logging.html
# 2. https://docs.python.org/2/howto/logging-cookbook.html
