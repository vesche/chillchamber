#!/usr/bin/env python

from setuptools import setup
from chillchamber.meta import VERSION

setup(
    name='chillchamber',
    packages=[
        'chillchamber',
        'chillchamber.apps',
        'chillchamber.images'
    ],
    package_data = {
        'chillchamber.images': ['*.png']
    },
    version=VERSION,
    description='chillchamber wip',
    license='MIT',
    url='https://github.com/vesche/chillchamber',
    author='Austin Jackson',
    author_email='vesche@protonmail.com',
    entry_points={
        'console_scripts': [
            'chillchamber = chillchamber.main:main',
        ]
    },
    install_requires=[
        'PySimpleGUI'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8'
    ]
)