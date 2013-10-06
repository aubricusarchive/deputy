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

from docopt import docopt

from deputy import config
from deputy import loaders
from deputy import utils
from deputy.exceptions import CasefileMissingError
from deputy.exceptions import CasefileConflictError

# Docopt handling

def main():
    args = docopt(
        __doc__, version=utils.get_version(), help=False, options_first=True
    )

    if args['--help']:
        sys.exit(print_help())

    if args['--list']:
        print(args)

    if args['<command>']:
        casefile_name = args['<command>']
        casefile_argv = [casefile_name] + args['<args>']

        try:
            run_casefile(casefile_name, casefile_argv)

        except CasefileConflictError:
            sys.exit("encountered a conflict.")

        except CasefileMissingError:
            sys.exit("could not find the casefile")

        else:
            sys.exit(0)


def print_help():
    print(__doc__)
    print_available_casefiles()


def print_available_casefiles():
    available_header          = 'Available casefiles:\n'
    available_casefile_format = '{name}\t{doc}'
    settings                  = config.load_config()
    load_entry_points         = loaders.get_entry_point_loader(settings)
    load_local_files          = loaders.get_file_system_loader(settings)

    print(available_header)

    # Print all available casefiles.
    for casefile in load_entry_points() + load_local_files():
        name, doc = casefile.name(), casefile.help()

        print(available_casefile_format.format(name=name, doc=doc))

    # Print newline.
    print()


def run_casefile(casefile_name, casefile_argv):
    settings          = config.load_config()
    load_entry_points = loaders.get_entry_point_loader(settings)
    load_local_files  = loaders.get_file_system_loader(settings)
    entry_points      = load_entry_points(casefile_name=casefile_name)
    local_files       = load_local_files(casefile_name=casefile_name)

    result = entry_points + local_files

    if len(result) == 1:
        casefile = result[0].load()
        casefile.run(casefile_argv)

    elif len(result) > 1:
        raise CasefileConflictError()

    else:
        raise CasefileMissingError()
        pass



# Main sys call

if __name__ == "__main__":
    sys.exit(main())
