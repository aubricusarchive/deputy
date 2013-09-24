from __future__ import absolute_import

# Debug only
# import pdb

import os
import sys
import unittest

from unittest import TestCase

sys.path.insert(0, os.path.abspath('../'))


def __run__(testcase, verbosity=2):
    loader = unittest.TestLoader()
    suite  = loader.loadTestsFromTestCase(testcase)
    runner = unittest.TextTestRunner(verbosity=verbosity)

    runner.run(suite)


class DeputyTestCase(TestCase):
    """Deputy unittest test suite."""

    def test_desk_search(self):
        """Test searching the deputy's desk."""
        pass

    def test_desk_is_empty(self):
        """Test searching an empty desk."""
        pass

    def test_filecabinet_search(self):
        """Test searching the deputy's file cabinet."""
        pass

    def test_filecabinet_is_empty(self):
        """Test searching an empty file cabinet."""
        pass

    def test_docket_collect_desk_casefiles(self):
        """Test collect a docket only from the desk."""
        pass

    def test_docket_collect_filecabinet_casefiles(self):
        """Test collect a docket only from the file cabinet."""
        pass

    def test_docket_collect_casefiles(self):
        """Test collect a docket."""
        pass

    def test_docket_list_tasks(self):
        """Test listing docket tasks."""
        pass

    def test_docket_get_task(self):
        """Test getting a task from the docket."""
        pass

    def test_deputy_task(self):
        """Test executing a deputy task."""
        pass

    def test_deputy_unknown_task(self):
        """Test executing an unknown task."""
        pass

    def test_deputy_help(self):
        """Test asking deputy for help."""
        pass

    def test_deputy_task_help(self):
        """Test asking deputy for help on a task."""
        pass


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
