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
from stevedore import driver


def main():
    # TODO: Hardcoded - Make this dynaic
    # This will probably be the plugin register / discovery step.
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
        plugin = driver.DriverManager(
            namespace='deputy.commands',
            name = command,
            invoke_on_load=True
        )

        plugin.driver.execute(command_argv)
    else:
        sys.exit(
            'Could not find the command "{}", please see deputy --help for more info.'
                .format(command))


if __name__ == "__main__":
    sys.exit(main())
