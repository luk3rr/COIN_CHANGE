#!/usr/bin/env python3

# Filename: __main__.py
# Created on: July  1, 2024
# Author: Lucas Araújo <araujolucas@dcc.ufmg.br>

import unittest

loader = unittest.TestLoader()
tests = loader.discover(start_dir='.', pattern='*_test.py')
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)
