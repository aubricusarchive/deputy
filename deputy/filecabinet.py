"""A deputy can get case files from anyone, not just the sheriff. Deputy will
check the file cabinet for additional case files defined by others.

"""

from pkg_resources import iter_entry_points

ENTRY_POINT_NAMESPACE = 'deputy.filecabinet'

def search(casefile_name):
    """Search the deputy's file cabinet for case files, \
    returns python module.
    """

    casefiles = collect()
    matching_result = None

    for casefile in casefiles:
        if casefile_name == casefile.name:
            matching_result = casefile
            break

    if matching_result is not None:
        return matching_result.load()

    else:
        raise NameError('Could not find matching name in file cabinet!')

# Helpers

def collect():
    """Collect case files (entry points) from the file cabinet."""

    casefiles = iter_entry_points(ENTRY_POINT_NAMESPACE)
    return casefiles
