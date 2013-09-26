from __future__ import absolute_import

# Debug only
# import pdb

import os
import sys
import unittest

from unittest import TestCase

from deputy import filecabinet

sys.path.insert(0, os.path.abspath('../'))


def __run__(testcase, verbosity=2):
    loader = unittest.TestLoader()
    suite  = loader.loadTestsFromTestCase(testcase)
    runner = unittest.TextTestRunner(verbosity=verbosity)

    runner.run(suite)


class DeputyTestCase(TestCase):
    """Deputy unittest test suite."""

    def test_filecabinet_collect(self):
        """Collect casefiles (entry points) from the file cabinet.

        This test requires deputy_lib is installed.
        """

        MOCK_CASEFILE_NAME = 'bang'
        casefiles = filecabinet.collect()

        try:
            casefile = next(casefiles)

        except StopIteration:
            self.fail('filecabinet.collect() returned no items!')

        self.assertEqual(
            casefile.name,
            MOCK_CASEFILE_NAME,
            msg='Casefile name should equal "bang".'
        )

    def test_filecabinet_search_matching(self):
        """Verify filecabinet.search properly imports \
        a known casefile module.

        This test requires deputy_lib is installed.
        """

        MOCK_CASEFILE_NAME = 'bang'

        try:
            search_result = filecabinet.search(MOCK_CASEFILE_NAME)

        except NameError:
            self.fail('filecabinet.search() returned no results!')

        self.assertTrue(
            search_result.__file__.endswith(MOCK_CASEFILE_NAME + '.pyc'),
            msg='Casefile module was not the correct module!'
        )

    def test_filecabinet_serach_name_errors(self):
        """Verify filecabinet.search rasises an error \
        with unknown casefile."""

        with self.assertRaises(NameError):
            filecabinet.search('unknown-casefile')

    # Helpers

    def get_mocks_dir():
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
