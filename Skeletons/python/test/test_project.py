#!/usr/bin/env python
import os
import sys
import unittest


sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/..')


from lib import Options


class TestProject(unittest.TestCase):
    def setUp(self):
        self.options = Options()

    def test_greeting(self):
        self.options.parse()
        self.assertEquals(self.options.known.name, 'World')


if __name__ == '__main__':
    unittest.main()
