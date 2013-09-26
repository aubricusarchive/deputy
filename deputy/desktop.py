"""You can leave casefiles for the deputy at her desk. She'll search
her desk (project-root/casefiles) for casefiles when looking for things to do.

"""

import os
import sys
import glob
import re
import importlib

# TODOs:

# - Refactor - Filecabinet and desktop have a lot of shared code with minor
# variations to handle the difference between loading an entry point
# and a raw python module. Possible to trim down?

# - Error Handling - Need to add better error handling for
# missing casefile dir.


CASEFILES_DIR_NAME = 'casefiles'
CASEFILES_DIR = os.getcwd() + '/' + CASEFILES_DIR_NAME


def search(casefile_name, casefiles_dir=CASEFILES_DIR):
    raw_casefiles = collect(casefiles_dir)
    matched_result = None

    for raw_casefile in raw_casefiles:
        if casefile_name in raw_casefile:
            matched_result = raw_casefile
            break

    if matched_result is not None:
            return import_raw_casefile(matched_result)
    else:
        # TODO: Revisit - Raise cutom error here.
        raise NameError('Could not find matching name on the desktop!')


def report(casefiles_dir=CASEFILES_DIR):
    """Report available casefiles."""

    raw_casefiles = collect(casefiles_dir)
    casefiles = [import_raw_casefile(raw_casefile) for raw_casefile in raw_casefiles]
    report = []

    # TODO: Similar Code - Similar code in deputy.filecabinet
    for casefile in casefiles:
        report.append(
            {
                'name': casefile.__name__,
                'doc': casefile.run.__doc__,
                'casefile': casefile
            }
        )

    return report


# Helpers
# ============================================================================

def collect(casefiles_dir=CASEFILES_DIR):
    """Collect case files (entry points) from the file cabinet."""


    casefiles = []

    # Filter out paths with dunder file names.
    filter_re = r'.*__.py$'

    try:
        casefiles = [ i for i in glob.glob(casefiles_dir + '/*.py') \
            if not re.search(filter_re, i)]

    # TODO: Revisit - Glob will not raise this error.
    except OSError:
        raise

    return casefiles

def import_raw_casefile(raw_casefile):
    path, file_name = raw_casefile.rsplit('/', 1)

    update_sys_path(path)

    try:
        casefile = importlib.import_module(file_name.strip('.py'))
    except ImportError:
        raise
    else:
        return casefile


def update_sys_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)
