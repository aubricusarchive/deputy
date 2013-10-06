"""Exceptions for deputy."""

class DeputyError(Exception):
    def __init__(self, msg="Message not set."):
         self.msg = msg


class CasefileMissingError(DeputyError):
    def __init__(self):
        super(CasefileMissingError, self).__init__()


class CasefileConflictError(DeputyError):
    def __init__(self):
        super(CasefileConflictError, self).__init__()

