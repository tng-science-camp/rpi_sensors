# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rpi_sensors',
    version='0.1.0',
    description='Raspberry Pi sensor library',
    long_description=readme,
    author='Seung H. Chung',
    author_email='auxplex@gmail.com',
    url='https://github.com/tng-science-camp/rpi_sensors',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
