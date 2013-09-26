"""A deputy can get case files from anyone, not just the sheriff. Deputy will
check the file cabinet for additional case files defined by others.

"""

from pkg_resources import iter_entry_points

# TODOs:
# - Refactor - Filecabinet and desktop have a lot of shared code with minor
# variations to handle the difference between loading an entry point
# and a raw python module. Possible to trim down?


ENTRY_POINT_NAMESPACE = 'deputy.filecabinet'


def search(casefile_name):
    """Search the deputy's file cabinet for case files, \
    returns python module.
    """

    raw_casefiles = collect()
    matched_result = None

    for raw_casefile in raw_casefiles:
        if casefile_name == raw_casefile.name:
            matched_result = raw_casefile
            break

    if matched_result is not None:
        return matched_result.load()

    else:
        # TODO: Revisit - Raise cutom error here.
        raise NameError('Could not find matching name in file cabinet!')

def report():
    """Report available casefiles."""

    raw_casefiles = list(collect())
    casefiles = [raw_casefile.load() for raw_casefile in raw_casefiles]
    report = []

    # TODO: Similar Code - Similar code in deputy.desktop
    for i, casefile in enumerate(casefiles):
        report.append(
            {
                'name': raw_casefiles[i].name,
                'doc': casefile.run.__doc__,
                'casefile': casefile
            }
        )

    return report


# Helpers
# ============================================================================

def import_raw_casefile(raw_casefile):
    try:
        raw_casefile.load()
    except ImportError:
        raise

def collect():
    """Collect case files (entry points) from the file cabinet."""

    raw_casefiles = iter_entry_points(ENTRY_POINT_NAMESPACE)
    return raw_casefiles
