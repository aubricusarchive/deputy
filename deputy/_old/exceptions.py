"""Exceptions for deputy."""

class DeputyError(Exception):
    def __init__(self, msg):
         self.msg = msg


class CasefileError(DeputyError):
    def __init__(self, *args):
        super(CasefileError, self).__init__(*args)
