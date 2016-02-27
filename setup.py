#!/usr/bin/env python
# coding: utf-8

from distutils.core import setup
from setuptools import find_packages

VERSION = __import__("admin_report").__version__

CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
]

install_requires = [
    'requirements.txt',
]

setup(
    name="django-admin-report",
    packages=find_packages(exclude=["tests"]),
    description="A Django library to create reports with Django ORM",
    version=VERSION,
    author="Mateus Vanzo de Padua",
    author_email="mateuspaduaweb@gmail.com",
    license='MIT License',
    platforms=['OS Independent'],
    url="https://github.com/mateuspadua/django-admin-report",
    keywords=[
        'report', 'django', 'admin', 'group_by',
        'annotate', 'agregate', 'ORM'
    ],
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)
