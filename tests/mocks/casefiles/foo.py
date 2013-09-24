"""
Usage: deputy foo [options]

options:
    -x      Do something custom!

short description: List system information.
"""

from docopt import docopt
from subprocess import call
import sys


def run(argv):
    """Foo bar baz qux!"""

    args = docopt(__doc__, argv)

    # Trivial example:
    # -x is NOT a standard uname option.
    #
    # If: -x is set do custom action.
    # Else: pass argv through.
    if args['-x']:
        sys.exit(call(['echo', 'foo bar baz qux!']))
