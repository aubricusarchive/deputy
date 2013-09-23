# TODO

[Docopt Git Example]: https://github.com/docopt/docopt/blob/master/examples/git/git.py
[Setuptools Docs]: https://pythonhosted.org/setuptools/setuptools.html
[Entry Points Docs]: http://pythonhosted.org/distribute/pkg_resources.html#entry-points

## v0.0.1 - v0.0.4

- ~~TODO: Create commandline with deputy as entrypoint.~~
- ~~TODO: Create basic sub-command example.~~
    - ~~Reference: [Docopt Git Example]~~
- ~~TOOD: Add command discovery~~
- ~~TODO: Add dynamic help string~~
    - ~~Need to see if -h can be overridden / extended.~~
- ~~TODO: Write fab --list equivelent~~
- ~~TODO: Move sys.exits to top level.~~
- ~~TODO: Return list instead of sys.exit from list_commands~~

## v0.0.5

- TODO: Write better command import.
- TODO: Use entry_points (setuptools) to allow other instlled libs extend deputy.
    - [Setuptools Docs]
    - [Entry Points Docs]
    - Other Resources:
        - ?
- TODO: Cleanup cli packge / scripts
    - List commands will need some clean up
    - Break out actions, reduce code in __init__.py

