from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os
import sys

import network_alert

here = os.path.abspath(os.path.dirname(__file__))

packages = ['network_alert']
requires = ['pytest']

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', 'test']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='network_alert',
    version='0.1',
    description='Discover new machines on your network.',
    author='Mike McCann',
    cmdclass={'test': PyTest},
    packages=packages,
    package_dir={'network_alert': 'network_alert'},
)