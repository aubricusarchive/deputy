"""
Usage: deputy [-v | --version]
       deputy [-h | --help]
       deputy [-l | --list]
       deputy <command> [<args>...]

Options:
    -h, --help           print deputy help message
    -v, --version        print deputy version
    -l, --list           print available deputy commands
"""

from __future__ import print_function

import sys
import importlib
import os
# import subprocess

from docopt import docopt


def main():
    args = docopt(
        __doc__, version='v0.0.4', help=False, options_first=True
    )

    if args['--help']:
        sys.exit(print_help())

    if args['--list']:
        print('')
        sys.exit(print_command_list())

    if args['<command>']:
        command_name = args['<command>']
        command_argv = [command_name] + args['<args>']

        sys.exit(execute_command(command_name, command_argv))


# Actions


def print_help():
    print(__doc__)
    print_command_list()


def print_command_list():
    commands = list_available_commands()
    print('Available commands:\n\n' + '\n'.join(commands) + '\n')


def execute_command(command_name, command_argv):
    module = import_command(command_name)
    module.run(command_argv)


# Helpers


def update_sys_path(cwd):
    # Add current working directory to PATH
    if cwd not in sys.path:
        sys.path.insert(0, cwd)


def import_command(command_name):
    cwd = os.getcwd()
    module = None

    update_sys_path(cwd)

    try:
        module = importlib.import_module('depfile.' + command_name)

    except ImportError:
        print('\nThere was a problem executing {}.'.format(command_name))
        sys.exit(print_help())

    return module


def list_available_commands():
    command_string = '{command_name}:\t{doc}'
    command_strings = []

    for i in scan_depfile():
        module = import_command(i)
        help_string = command_string.format(
            command_name=i,
            doc=module.run.__doc__
        )

        command_strings.append(help_string)

    return command_strings


def scan_depfile():
    excludes = ['.DS_Store', '__init__.py']

    cwd = os.getcwd()

    # TODO: Hardcoded, make configurable
    commands_dir = cwd + '/depfile'
    commands = []

    try:
        os.listdir(commands_dir)

    except OSError:
        sys.exit('No depfile found in ' + cwd)

    for i in os.listdir(commands_dir):

        if(i.endswith('.pyc') or i in excludes):
            continue

        commands.append(i.strip('.py'))

    return commands


# Main sys call

if __name__ == "__main__":
    sys.exit(main())
