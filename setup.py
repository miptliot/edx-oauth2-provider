#!/usr/bin/env python

from setuptools import find_packages, setup

import edx_oauth2_provider

setup(
    name='edx-oauth2-provider',
    version=edx_oauth2_provider.__version__,
    description='Provide OAuth2 access to edX installations',
    author='edX',
    url='https://github.com/edx/edx-oauth2-provider',
    license='AGPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'django>=2.0.1',
        'PyJWT>=1.4.0,<2.0.0'
    ]
)
