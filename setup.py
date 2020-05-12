#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setuptools script for flake8-html."""

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'jinja2>=2.9.0',
    'pygments>=2.2.0',
    'flake8>=3.3.0',
    'importlib-metadata;python_version<"3.8"',
]

test_requirements = [
    'tox',
    'pytest'
]

setup(
    name='flake8-html',
    version='0.4.0',
    description="Generate HTML reports of flake8 violations",
    long_description=readme + '\n\n' + history,
    author="Daniel Pope",
    author_email='mauve@mauveweb.co.uk',
    url='https://github.com/lordmauve/flake8-html',
    packages=[
        'flake8_html',
    ],
    package_dir={'flake8_html': 'flake8_html'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    entry_points={
        'flake8.report': [
            'html = flake8_html:HTMLPlugin',
        ]
    },
    zip_safe=False,
    keywords='flake8 html',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flake8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
