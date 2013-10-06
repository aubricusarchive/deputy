from pkg_resources import iter_entry_points
from deputy import utils


class EntryPointService(object):

    def __init__(self):
        super(EntryPointService, self).__init__()

    def iter_casefiles(self, search_location):
        return iter_entry_points(search_location)


class FileSystemService(object):

    def __init__(self):
        super(FileSystemService, self).__init__()

    def iter_casefiles(self, search_location):
        return utils.glob_casefiles(search_location)


def get_service_for_type(casefile_type):
    if(casefile_type == 'entry_point'):
        return EntryPointService

    if(casefile_type == 'file_system'):
        return FileSystemService

    raise NameError('unsupported casefile type')
