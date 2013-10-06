from __future__ import absolute_import

import os
import sys
import unittest
from warnings import warn

from unittest import TestCase

from deputy import loaders
from deputy import config


sys.path.insert(0, os.path.abspath('../'))

def __run__(testcase, verbosity=2):
    loader = unittest.TestLoader()
    suite  = loader.loadTestsFromTestCase(testcase)
    runner = unittest.TextTestRunner(verbosity=verbosity)

    runner.run(suite)


class DeputyTestCase(TestCase):
    """Deputy unittest test suite."""

    def setUp(self):
        self.settings = config.load_config()


    def test_load_default_config(self):
        """Test that the default config loads properly."""

        expected_defaults = {
            'casefiles_dir': os.getcwd() + '/casefiles',
            'casefiles_entry_point': 'deputy.casefiles',
        }

        settings = config.load_config()

        self.assertEqual(expected_defaults, settings)

    def test_iter_entrypoints_with_default_config(self):
        """Test basic setup.py entry_point config."""

        from deputy import config
        from pkg_resources import iter_entry_points

        settings                  = config.load_config()
        entry_points              = iter_entry_points(settings['casefiles_entry_point'])
        expected_entry_point_name = 'bang'
        depends_on                = 'deputy_lib'

        try:
            __import__(depends_on)
            self.assertEqual(entry_points.next().name, expected_entry_point_name)

        except ImportError:
            warn('Skipping test, deputy_lib is not available.')

    def test_get_all_entry_points(self):
        """Test get all entry points."""

        load_casefiles          = loaders.get_entry_point_loader(self.settings)
        casefiles               = load_casefiles()
        casefile_names          = sorted([x.name() for x in casefiles])
        expected_casefile_names = sorted(['bang', 'bash', 'pop'])
        depends_on              = 'deputy_lib'

        try:
            __import__(depends_on)
            self.assertEqual(casefile_names, expected_casefile_names)

        except ImportError:
            warn('Skipping test, deputy_lib is not available.')

    def test_get_specific_entry_point(self):
        """Test get a specific entry point."""

        load_casefiles          = loaders.get_entry_point_loader(self.settings)
        casefiles               = load_casefiles(casefile_name='bang')
        casefile_names          = sorted([x.name() for x in casefiles])
        expected_casefile_names = sorted(['bang'])
        depends_on              = 'deputy_lib'

        try:
            __import__(depends_on)
            self.assertEqual(casefile_names, expected_casefile_names)

        except ImportError:
            warn('Test depends on deputy_lib')

    def test_get_all_files(self):
        """Test get all files."""

        self.settings['casefiles_dir'] = self.get_mocks_dir() + '/casefiles'

        load_casefiles            = loaders.get_file_system_loader(self.settings)
        casefiles                 = load_casefiles()
        casefile_names            = sorted([x.name() for x in casefiles])
        expected_casefile_names = sorted(['uname', 'kelly'])

        self.assertEqual(casefile_names, expected_casefile_names)

    def test_get_specific_file(self):
        """Test get a specifi file."""

        self.settings['casefiles_dir'] = self.get_mocks_dir() + '/casefiles'

        load_casefiles            = loaders.get_file_system_loader(self.settings)
        casefiles                 = load_casefiles(casefile_name='kelly')
        casefile_names            = sorted([x.name() for x in casefiles])
        expected_casefile_names = sorted(['kelly'])

        self.assertEqual(casefile_names, expected_casefile_names)

# Helpers

    def get_mocks_dir(self):
        """Helper to return mocks directory.

        returns string
        raises OSError if directory is not found.
        """

        test_dir = os.path.dirname(os.path.realpath(__file__))
        mocks_dir = test_dir + '/mocks'

        try:
            os.listdir(mocks_dir)
        except OSError:
            raise
        else:
            return mocks_dir


if __name__ == '__main__':
    __run__(DeputyTestCase, verbosity=2)
