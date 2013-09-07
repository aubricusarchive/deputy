"""Usage:
    deputy foo
    deputy foo [-o | --opt]
    deputy foo <arg>
    deputy [-h | --help]

    Lorem ipsum dolor.

    Examples:
        $ deputy foo
        $ deputy foo -o | --opt

    Arguments
        <arg>           Example arguments.

    Options:
        -o --opt        Example option.
        -h --help       Displays this message.
"""

import sys
from docopt import docopt


def main():
    arguments = docopt(__doc__)

    print(arguments)


if __name__ == "__main__":
    sys.exit(main())
