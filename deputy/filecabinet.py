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
    matched_result = None

    for raw_casefile in casefiles:
        if casefile_name == raw_casefile.name:
            matched_result = raw_casefile
            break

    if matched_result is not None:
        return matched_result.load()

    else:
        # TODO: Revisit - Raise cutom error here.
        raise NameError('Could not find matching name in file cabinet!')

# Helpers

def collect():
    """Collect case files (entry points) from the file cabinet."""

    casefiles = iter_entry_points(ENTRY_POINT_NAMESPACE)
    return casefiles
