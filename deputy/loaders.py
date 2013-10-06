from functools import partial
from pkg_resources import iter_entry_points

from deputy import utils
from deputy.casefile import EntryPointCasefile
from deputy.casefile import FileSystemCasefile


def load_casefile(casefile_type, search_location, casefile_name='*'):
    casefile_list = []

    if casefile_type == 'entry_point':
        eps = iter_entry_points(search_location)

        for ep in eps:
            casefile = EntryPointCasefile(ep)

            if(casefile_name == '*'):
                casefile_list.append(casefile)
                continue

            elif(casefile_name == casefile.name()):
                casefile_list.append(casefile)
                break

    if casefile_type == 'filesystem':
        files = utils.glob_casefiles(search_location)

        for f in files:
            casefile = FileSystemCasefile(f)

            if(casefile_name == '*'):
                casefile_list.append(casefile)
                continue

            elif(casefile_name == casefile.name()):
                casefile_list.append(casefile)
                break


    return casefile_list


def get_entry_point_loader(settings):
    return partial(
        load_casefile,
        casefile_type='entry_point',
        search_location=settings['casefiles_entry_point']
    )


def get_file_system_loader(settings):
    return partial(
        load_casefile,
        casefile_type='filesystem',
        search_location=settings['casefiles_dir']
    )


def get_custom_loader(*args, **kwargs):
    return partial(load_casefile, *args, **kwargs)


