"""
Usage: deputy bang [options]

options:
    -x      Do something custom!

short description: List system information.
"""

from docopt import docopt
from subprocess import call
import sys


def run(argv):
    """Bang Bang Bang!!!"""

    args = docopt(__doc__, argv)

    if args['-x']:
        call(['echo', 'bang bang bang!!!'])
