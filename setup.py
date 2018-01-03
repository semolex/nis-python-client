#!/usr/bin/env python
__copyright__ = "2017 Oleksii Semeshchuk"
__license__ = "License: MIT, see LICENSE."

'''
    setup
    _____
'''

from setuptools import setup
import unittest

DESCRIPTION = 'Python client for NEM NIS API (https://nemproject.github.io)'

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: Unix',
    'Operating System :: POSIX :: Linux',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet :: WWW/HTTP',
    'Framework :: AsyncIO',
]

def test_suite():
    loader = unittest.TestLoader()
    suite = loader.discover('test', pattern='test_*.py')
    return suite


setup(
    name='nis-python-client',
    version='0.0.9',
    description=DESCRIPTION,
    classifiers=CLASSIFIERS,
    author='semolex (Oleksii Semeshchuk)',
    author_email='semolex@live.com',
    packages=['nemnis'],
    url='https://github.com/semolex/nis-python-client',
    license='MIT',
    test_suite='setup.test_suite',
    zip_safe=True,
    install_requires=[
        'requests==2.18.4',
        'six',
    ],
    test_requires=[
        'requests-mock==1.4.0',
    ],
)
