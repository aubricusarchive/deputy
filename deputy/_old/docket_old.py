"""A docket collects all of the deputy's casefiles."""

import os

from deputy import filecabinet
from deputy import desktop


CASEFILES_DIR_NAME = 'casefiles'
CASEFILES_DIR = os.getcwd() + '/' + CASEFILES_DIR_NAME


def report(casefiles_dir=CASEFILES_DIR):
    """Collect all available case files."""

    return filecabinet.report() + desktop.report(casefiles_dir)


def search(casefile_name, casefiles_dir=CASEFILES_DIR):
    casefile_list = report()

    for casefile_info in casefile_list:
        if casefile_name == casefile_info['name']:
            return casefile_info['casefile']

    # if we get here, we found 0 matches
    raise NameError('Could not find any matching casefiles in the docket!')
