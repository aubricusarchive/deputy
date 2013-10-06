"""
Usage: deputy [-v | --version]
       deputy [-h | --help]
       deputy [-l | --list]
       deputy <command> [<args>...]

Options:
    -h, --help     print deputy help message
    -v, --version  print deputy version
    -l, --list     print available deputy commands
"""

from __future__ import print_function

import sys

from itertools import chain

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
        sys.exit(print_available_casefiles())

    if args['<command>']:
        casefile_name = args['<command>']
        casefile_argv = [casefile_name] + args['<args>']

        try:
            run_casefile(casefile_name, casefile_argv)

        except CasefileConflictError:
            sys.exit("encountered a conflict with another casefile.")

        except CasefileMissingError:
            sys.exit("could not find that casefile.")

        else:
            sys.exit(0)

# Actions

def print_help():
    print(__doc__)
    print_available_casefiles()


def print_available_casefiles():
    available_header          = 'Available casefiles:\n'
    available_casefile_format = '{name}\t{doc}'
    settings                  = config.load_config()
    casefile_loaders          = loaders.get_loaders(settings)

    # TODO: Revisit, call to chain here is a bit clunky
    casefiles = [ldr() for ldr in casefile_loaders]
    casefiles = chain(*casefiles)

    print(available_header)

    for casefile in casefiles:
        name, doc = casefile.name(), casefile.help()

        print(available_casefile_format.format(name=name, doc=doc))

    # Print newline.
    print()


def run_casefile(casefile_name, casefile_argv):
    settings          = config.load_config()

    # TODO: Revisit, super ugly.
    casefile_loaders = loaders.get_loaders(settings)
    casefiles = [ldr(casefile_name=casefile_name) for ldr in casefile_loaders]
    casefiles = chain(*casefiles)
    casefiles = list(casefiles)

    if len(casefiles) == 1:
        casefile = casefiles[0].load()
        casefile.run(casefile_argv)

    elif len(casefiles) > 1:
        raise CasefileConflictError()

    else:
        raise CasefileMissingError()
        pass

# Main sys call

if __name__ == "__main__":
    sys.exit(main())
