"""
Usage: deputy [-v | --version]
       deputy [--help]
       deputy <command> [<args>...]

options:
   -h, --help           print deputy help message
   -v, --version        print deputy version


See 'deputy help <command>' for more information on a specific command.
"""

import sys

from docopt import docopt


def main():
    commands = ['uname']
    # import_root = 'deputy.cli.'

    args = docopt(
        __doc__,
        version='v0.0.1',
        options_first=True
    )

    print('Global arguments: ')
    print(args)

    # Assemble argument vector
    argv = [args['<command>']] + args['<args>']

    # if args['<command>'] == 'uname':
    #     from deputy.cli import utils
    #     sys.exit(utils.exe(argv))
    #

    if args['<command>'] in commands:
        # command = import_root + args['<command>']
        # print(command)
        # import imp
        # f, fn, desc = imp.find_module('deputy')
        # pkg_deputy = imp.load_module('deputy', f, fn, desc)
        # f, fn, desc = imp.find_module('cli', pkg_deputy.__path__)
        # pkg_cli = imp.load_module('cli', f, fn, desc)
        # f, fn, desc = imp.find_module('uname', pkg_cli.__path__)

        # module = imp.load_module('deputy.cli.uname', f, fn, desc)
        # print(module)
        # print(dir(module))

        #
        # import deputy.cli.uname as uname
        # print(uname)
        # print(dir(uname))
        #
        import importlib
        result = importlib.import_module('deputy.cli.uname')
        print(result)
        print(dir(result))
        result.exe(argv)


if __name__ == "__main__":
    sys.exit(main())
