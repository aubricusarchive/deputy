import sys
import importlib

class EntryPointCasefile(object):
    """A casefile derived from an entry point."""

    def __init__(self, raw_casefile):
        super(EntryPointCasefile, self).__init__()
        self.raw_casefile = raw_casefile

    def name(self):
        """Return the casefile name."""
        return self.raw_casefile.name

    def help(self):
        """Return the casefile main's __doc__ string."""
        return self.load().run.__doc__

    def load(self):
        """Import the casefile."""

        try:
            return self.raw_casefile.load()

        except ImportError:
            raise


class FileSystemCasefile(object):
    """A casefile derived from a local file."""

    def __init__(self, raw_casefile):
        super(FileSystemCasefile, self).__init__()
        self.raw_casefile = raw_casefile

    def name(self):
        """Return the casefile name."""

        return self.get_file_path_components(self.raw_casefile)['name']

    def help(self):
        """Return the casefile main's __doc__ string."""
        return self.load().run.__doc__

    def load(self):
        """Import the casefile."""
        raw_components = self.get_file_path_components(self.raw_casefile)
        path           = raw_components['path']
        name           = raw_components['name']

        # update sys path
        if path not in sys.path:
            sys.path.insert(0, path)

        try:
            return importlib.import_module(name)
        except ImportError:
            raise

    def get_file_path_components(self, file_location):
        path, file_name = file_location.rsplit('/', 1)
        name, extension = file_name.rsplit('.', 1)

        return {
            'path':      path,
            'file_name': file_name,
            'name':      name,
            'extension': extension
        }

