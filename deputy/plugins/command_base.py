# deputy/plugins/a_command.py

import abc


class CommandBase(object):
    """Base class for a basic command."""

    __metaclass__ = abc.ABCMeta


    def __init__(self):
        pass


    @abc.abstractmethod
    def execute(self, argv):
        """Excutes the command.

        :param argv: the argument vector for the command.
        :returns None
        """

