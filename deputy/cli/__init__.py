"""
Usage: deputy [-v | --version]
       deputy [--help]
       deputy <command> [<args>...]

options:
    -h, --help           print deputy help message
    -v, --version        print deputy version
"""

import sys
import importlib

from docopt import docopt


def main():
    # TODO: Hardcoded - Make this dynaic
    commands = ['uname']

    args = docopt(
        __doc__,
        version='v0.0.1',
        options_first=True
    )

    command = args['<command>']
    command_args = args['<args>']
    command_argv = [command] + command_args

    if command in commands:
        result = importlib.import_module('deputy.commands.' + command)
        result.exe(command_argv)


if __name__ == "__main__":
    sys.exit(main())
