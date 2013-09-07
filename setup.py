#!/usr/bin/env python

import os
import sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

deputys = [
    'deputy'
]

deputy_data = {'deputy': ['LICENSE.md', 'README.md']}

requires = [
    'setuptools',
    'docopt==0.6.1'
]

entry_points = {
    'console_scripts': ['deputy = deputy.cli:main']
}

setup(
    url='http://github.com/aubricus/deputy',
    name='deputy',
    version='0.0.1u',
    description='Lorem ipsum dolor',
    author='Aubrey Taylor',
    author_email='aubricus@gmail.com',
    deputys=deputys,
    deputy_data=deputy_data,
    install_requires=requires,
    entry_points=entry_points,
    deputy_dir={'deputy': 'deputy'},
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

)

del os.environ['PYTHONDONTWRITEBYTECODE']
