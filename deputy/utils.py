import glob
import re

def glob_casefiles(target_dir):
    """Glob casefile filenames for target_dir."""

    file_names = []
    filter_re = r'__.py$' # filter out dunder files

    file_glob = glob.glob(target_dir + '/*.py')

    file_names = [
        file_name for file_name in file_glob \
        if not re.search(filter_re, file_name)
    ]

    return file_names
