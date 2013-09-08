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
import os
import subprocess

from docopt import docopt


def main():
    commands = get_commands()
    print(commands)

    args = docopt(
        __doc__,
        version='v0.0.1',
        options_first=True
    )

    command = args['<command>']
    command_args = args['<args>']
    command_argv = [command] + command_args

    if command in commands:
        command_module = importlib.import_module('depfile.' + command)
        print(command_module.__doc__)
        command_module.exe(command_argv)
    else:
        print("'{}' is not a registered deputy.py command.\n".format(command))
        sys.exit(subprocess.call(['deputy', '--help']))


def get_commands():
    cwd = os.getcwd()
    plugin_dir = cwd + '/depfile'
    plugins = []

    # Add current working directory to PATH
    if cwd not in sys.path:
        sys.path.insert(0, cwd)

    for i in os.listdir(plugin_dir):
        if(i.endswith('.pyc') or i == "__init__.py"):
            continue

        plugins.append(i.strip('.py'))

    return plugins

if __name__ == "__main__":
    sys.exit(main())
