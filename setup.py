#!/usr/bin/env python
import os
import sys
from setuptools import setup

# ex: python setup.py publish
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

# Python won’t try to write .pyc or .pyo files on the import of source modules.
# see: http://docs.python.org/2/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

packages = [
    'deputy'
]

requires = []

setup(
    name='deputy',
    version='0.0.0',
    description='Generate a random roll from a n-number of an n-sided die',
    long_description=open('README.md').read(),
    author='Aubrey Taylor',
    author_email='aubricus@gmail.com',
    url='http://github.com/aubricus/deputy',
    license=open('LICENSE.md').read(),
    packages=packages,
    package_data={'': ['LICENSE.md']},
    include_package_data=True,
    install_requires=requires,
    package_dir={'deputy': 'deputy'},
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),

)

del os.environ['PYTHONDONTWRITEBYTECODE']