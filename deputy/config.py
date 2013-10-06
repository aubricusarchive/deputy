import os

# TODO:
# - Idea, make config file driven. Made stubs to that effect.

def load_config(config_location=None):
    if config_location is None:
        cwd = os.getcwd()
        casefiles_dir_name = 'casefiles'
        casefiles_dir = cwd + '/' + casefiles_dir_name

        return {
            'casefiles_dir': casefiles_dir,
            'casefiles_entry_point': 'deputy.casefiles'
        }

    else:
        # load config
        # return settings
        pass
