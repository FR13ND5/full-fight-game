#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import shutil
import sys

from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

version = get_version('ffgame')

if sys.argv[-1] == 'publish':
    # if os.system("pip freeze | grep wheel"):
    #     print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
    #     sys.exit()
    # if os.system("pip freeze | grep twine"):
    #     print("twine not installed.\nUse `pip install twine`.\nExiting.")
    #     sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    # os.system("twine upload dist/*")
    # print("You probably want to also tag the version now:")
    # print("  git tag -a %s -m 'version %s'" % (version, version))
    # print("  git push --tags")
    # shutil.rmtree('dist')
    # shutil.rmtree('build')
    # shutil.rmtree('full-fight-game.egg-info')
    sys.exit()


setup(
    name='full-fight-game',
    version=version,
    url="https://github.com/FR13ND5/full-fight-game",
    license='MIT',
    description='This is a simple game like a RPG to enjoy with your friends',
    author='Alexandre Proença, Yuri Reis, Lineu Felipe',
    author_email='alexandre.proenca@hotmail.com.br',  # SEE NOTE BELOW (*)
    packages=get_packages('ffgame'),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'robot_rest=ffgame.server:main',
        ],
    },
    zip_safe=False,
    keywords='RPM console game',


    package_data={
        'ffgame': ['*.tpl'],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console Environment',
        'Framework :: Core Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)

# (*) Please direct queries to the discussion group, rather than to me directly
#     Doing so helps ensure your question is helpful to other users.
#     Queries directly to my email are likely to receive a canned response.
#
#     Many thanks for your understanding.
