#!/usr/bin/env python

import os, sys
from setuptools import setup

from deputy import utils as deputy_utils

# Setup command helpers

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

# Setup arg values

url              = 'http://github.com/aubricus/deputy'
name             = 'deputy'
version          = deputy_utils.get_version()
description      = 'A person whose immediate superior is a senior figure within an organization and who is empowered to act as a substitute for this superior.'
author           = 'Aubrey Taylor'
author_email     = 'aubricus@gmail.com'
packages         = ['deputy']
package_data     = {'deputy': ['LICENSE.md', 'README.md']}
package_dir      = {'deputy': 'deputy'}
long_description = open('README.rst').read()
zip_safe         = False

requires = [
    'setuptools',
    'docopt==0.6.1'
]
entry_points = {
    'console_scripts': [
        'dep = deputy.cli:main'
    ],
    'deputy.casefiles': []
}
classifiers=(
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
)

setup(
    url=url,
    name=name,
    version=deputy_utils.get_version(),
    description=description,
    author=author,
    author_email=author_email,
    packages=packages,
    package_data=package_data,
    install_requires=requires,
    entry_points=entry_points,
    package_dir=package_dir,
    long_description=long_description,
    classifiers=classifiers,
    zip_safe=zip_safe,
)

del os.environ['PYTHONDONTWRITEBYTECODE']
