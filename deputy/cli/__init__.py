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
import subprocess

from docopt import docopt


def main():
    args = docopt(
        __doc__, version='v0.0.3', help=False, options_first=True
    )

    if args['--help']:
        print_help()

    if args['--list']:
        list_commands()

    if args['<command>']:
        command_name = args['<command>']
        command_argv = [command_name] + args['<args>']

        execute_command(command_name, command_argv)

# Actions
def print_help():
    print(__doc__)

    # TODO: See, todo @ list_commands
    subprocess.call(['deputy', '-l'])
    sys.exit()


def list_commands():
    help_string_format = '{command_name}:\t{doc}'
    help_strings = []

    for i in scan_depfile():
        module = import_command(i)
        help_string = help_string_format.format(
            command_name=i,
            doc=module.run.__doc__
        )

        help_strings.append(help_string)

    # TODO: Revisit, might be better to return something from this function.
    sys.exit('\nAvailable commands:\n\n' + '\n'.join(help_strings) + '\n')


def execute_command(command_name, command_argv):
    # command_names = scan_depfile();

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
        print('\nThere was a problem executing {}.\n'.format(command_name))
        subprocess.call(['deputy', '-h'])
        subprocess.call(['deputy', '-l'])
        sys.exit()

    return module


def scan_depfile():
    excludes = ['.DS_Store']

    cwd = os.getcwd()

    # TODO: Hardcoded, make configurable
    commands_dir = cwd + '/depfile'
    commands = []

    try:
        os.listdir(commands_dir)
    except OSError:
        sys.exit('No depfile found in ' + cwd)

    for i in os.listdir(commands_dir):
        # TODO: Cleanup, dirty
        if(i.endswith('.pyc') or i == "__init__.py" or i in excludes):
            continue

        commands.append(i.strip('.py'))

    return commands


# Main sys call

if __name__ == "__main__":
    sys.exit(main())
