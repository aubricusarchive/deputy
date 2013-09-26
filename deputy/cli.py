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

from deputy import docket

# Docopt
# ============================================================================

def main():
    args = docopt(
        __doc__, version='v0.0.4', help=False, options_first=True
    )

    if args['--help']:
        sys.exit(print_help())

    if args['--list']:
        print('')
        sys.exit(print_available_casefiles())

    if args['<command>']:
        casefile_name = args['<command>']
        casefile_argv = [casefile_name] + args['<args>']

        sys.exit(run_casefile(casefile_name, casefile_argv))


# Actions
# ============================================================================


def print_help():
    print(__doc__)
    print_available_casefiles()


def print_available_casefiles():
    available_header = 'Available casefiles:\n'
    available_casefile_format = '{name}\t{doc}'
    casefiles_list = docket.report()

    print(available_header)

    for casefile_info in casefiles_list:
        print(available_casefile_format.format(**casefile_info))

    # Insert newline
    print()


def run_casefile(casefile_name, casefile_argv):
    try:
        casefile = docket.search(casefile_name)
    except NameError:
        # TODO: Enhance - Print nice message.
        raise
    else:
        casefile.run(casefile_argv)


# Main sys call
# ============================================================================

if __name__ == "__main__":
    sys.exit(main())
