from functools import partial

from deputy import services
from deputy import containers


def loader(casefile_type, search_location, casefile_name='*'):
    container_list    = []
    CasefileContainer = containers.get_container_for_type(casefile_type)
    CasefileService   = services.get_service_for_type(casefile_type)

    service      = CasefileService()
    iter_results = service.iter_casefiles(search_location)

    for result in iter_results:
        container = CasefileContainer(result)

        if(casefile_name == '*'):
            container_list.append(container)
            continue

        elif(casefile_name == container.name()):
            container_list.append(container)
            break

    return container_list


def get_entry_point_loader(settings):
    return partial(
        loader,
        casefile_type='entry_point',
        search_location=settings['casefiles_entry_point']
    )


def get_file_system_loader(settings):
    return partial(
        loader,
        casefile_type='file_system',
        search_location=settings['casefiles_dir']
    )
