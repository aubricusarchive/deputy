"""
Usage: deputy kelly [options]

options:
    -x      Do something custom!
"""

from docopt import docopt
from subprocess import call


def run(argv):
    """Print system information."""

    args = docopt(__doc__, argv)

    if args['-x']:
        call(['echo', 'Kelly is cute!'])
