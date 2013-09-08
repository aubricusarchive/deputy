"""usage: deputy uname [options]

    Options:
    -a      Behave as though all of the options -mnrsv were specified.
    -m      print the machine hardware name.
    -n      print the nodename
    -p      print the machine processor architecture name.
    -r      print the operating system release.
    -s      print the operating system name.
    -v      print the operating system version.
"""
from docopt import docopt
from subprocess import call
import sys


def exe(argv):
    args = docopt(
        __doc__,
        argv
    )

    print('Argument Vector: ')
    print(argv)

    print('Command Arguments: ')
    print(args)

    print('Calling uname: ')
    sys.exit(call(argv))


