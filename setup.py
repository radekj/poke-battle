#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='pokebattle',
    version='0.0.1',
    url='https://github.com/skooda/poke-battle',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        "nameko>=2.1.2",
        "nameko_sqlalchemy>=0.0.1",
    ],
)
