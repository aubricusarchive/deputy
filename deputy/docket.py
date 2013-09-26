"""A docket collects all of the deputy's casefiles."""


def search(casefile_name, filecabinets=()):
    casefile_list = [x.report() for x in filecabinets]

    for casefile_info in casefile_list:
        if casefile_name == casefile_info['name']:
            return casefile_info['casefile']

    # if we get here, we found 0 matches
    raise NameError('Could not find any matching casefiles in the docket!')
