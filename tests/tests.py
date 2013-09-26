from __future__ import absolute_import

import os
import sys
import unittest

from unittest import TestCase

from deputy import filecabinet
from deputy import desktop
from deputy import docket

sys.path.insert(0, os.path.abspath('../'))


def __run__(testcase, verbosity=2):
    loader = unittest.TestLoader()
    suite  = loader.loadTestsFromTestCase(testcase)
    runner = unittest.TextTestRunner(verbosity=verbosity)

    runner.run(suite)


class DeputyTestCase(TestCase):
    """Deputy unittest test suite."""


# Filecabinet Tests
# ============================================================================

    ## TODOs:
    # - Finish report test

    def test_filecabinet_collect(self):
        """Collect casefiles (entry points) from the file cabinet.

        This test requires deputy_lib is installed.
        """

        MOCK_CASEFILE_NAME = 'bang'
        casefiles = filecabinet.collect()

        try:
            raw_casefile = next(casefiles)

        except StopIteration:
            self.fail('filecabinet.collect() returned no items!')

        self.assertEqual(
            raw_casefile.name,
            MOCK_CASEFILE_NAME,
            msg='Casefile name should equal "bang".'
        )

    def test_filecabinet_search_known(self):
        """Verify file cabinet.search properly imports \
        a known case file module.

        This test requires deputy_lib is installed.
        """

        MOCK_CASEFILE_NAME = 'bang'

        try:
            search_result = filecabinet.search(MOCK_CASEFILE_NAME)

        except NameError:
            self.fail('filecabinet.search() returned no results!')

        # Ensure the proper file was loaded.
        # TODO: Revisit - Maybe not the best test ever.
        # - __name__ instead?
        self.assertTrue(
            search_result.__file__.endswith(MOCK_CASEFILE_NAME + '.pyc'),
            msg='Casefile module was not the correct module!'
        )

    def test_filecabinet_serach_unknown(self):
        """Verify filecabinet.search rasises an error \
        with unknown case file."""

        with self.assertRaises(NameError):
            filecabinet.search('unknown-casefile')

    def test_filecabinet_report(self):
        """Verify report returns a list of known case files."""
        filecabinet.report()

# Desk tests
# ============================================================================

    # TODOs:
    # - Write test to verify collect glob filter is working correctly.
    # - Write test to verify missing casefile dir is handled correctly.
    # - Finish report test

    def test_desktop_collect(self):
        """Collect case files (modules) from the desk."""

        MOCK_CASEFILE_NAME = 'uname'
        CASEFILES_DIR = self.get_mocks_dir() + '/casefiles'
        casefiles = desktop.collect(casefiles_dir=CASEFILES_DIR)
        raw_casefile = casefiles[0]

        self.assertTrue(MOCK_CASEFILE_NAME in raw_casefile)

    def test_desktop_search_known(self):
        """Verify desk.search properly imports \
        a known case file module."""

        MOCK_CASEFILE_NAME = 'uname'
        CASEFILES_DIR = self.get_mocks_dir() + '/casefiles'
        search_result = desktop.search(
            MOCK_CASEFILE_NAME,casefiles_dir=CASEFILES_DIR)

        # Ensure the proper file was loaded.
        # TODO: Revisit - Maybe not the best test ever.
        # - __name__ instead?
        self.assertTrue(
            search_result.__file__.endswith(MOCK_CASEFILE_NAME + '.pyc'),
            msg='Casefile module was not the correct module!'
        )

    def test_desktop_search_unknown(self):
        """Verify desk.search raises an error \
        with unknown case file."""

        with self.assertRaises(NameError):
            desktop.search('unknown-casefile')

    def test_desktop_report(self):
        """Verify report returns a list of known case files."""
        CASEFILES_DIR = self.get_mocks_dir() + '/casefiles'
        desktop.report(CASEFILES_DIR)


# Docket tests
# ============================================================================

    # TODOs:
    # - Finish report tests
    # - Finish search tests

    def test_docket_search(self):
        pass

    def test_docket_report(self):
        CASEFILES_DIR = self.get_mocks_dir() + '/casefiles'
        casefile_list = docket.report(CASEFILES_DIR)

# Helpers
# ============================================================================

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
    __run__(DeputyTestCase, verbosity=0)
