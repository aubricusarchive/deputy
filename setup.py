#!/usr/bin/env python

import os, sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

package_data = {'deputy': ['LICENSE.md', 'README.md']}

requires = [
    'setuptools',
    'docopt==0.6.1',
    'stevedore'
]

entry_points = {
    'console_scripts': ['deputy = deputy.cli:main'],
    'deputy.commands': [
        'uname = deputy.commands.uname:Uname'
    ]
}

setup(
    url='http://github.com/aubricus/deputy',
    name='deputy',
    version='0.0.1u',
    description='A person whose immediate superior is a senior figure within an organization and who is empowered to act as a substitute for this superior.',
    author='Aubrey Taylor',
    author_email='aubricus@gmail.com',
    packages=['deputy'],
    package_data=package_data,
    install_requires=requires,
    entry_points=entry_points,
    package_dir={'deputy': 'deputy'},
    long_description=open('README.rst').read(),
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
    zip_safe=False,
)

del os.environ['PYTHONDONTWRITEBYTECODE']
