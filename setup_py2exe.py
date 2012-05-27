#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import py2exe

INSTALL_REQUIRES = [
    'PyYAML==3.10',
    'Twisted==12.0.0',
    'certifi==0.0.8',
    'chardet==1.0.1',
    'leftronic==1.4',
    'pyOpenSSL==0.13',
    'requests==0.11.1',
    'wsgiref==0.1.2',
    'zope.interface==3.8.0',
#    'MySQL-python==1.2.3',
    'SQLAlchemy==0.7.7',
#    'pyodbc==3.0.3',
    # remove database-specific driver packages; those should be installed separately with pip
]

try:
    import json
except ImportError:
    INSTALL_REQUIRES.append('simplejson')

setup(
    name='leftronicd_db',
    #packages=find_packages(),
    #include_package_data=True,
    #install_requires=INSTALL_REQUIRES,
    console=[{'script':'leftronicd/main.py'}],
    options={'py2exe': {
                'includes': ['twisted', 'certifi', 'chardet', 'leftronic',
                                'OpenSSL', 'requests', 'wsgiref', 'zope.interface', 
                                'sqlalchemy', 'yaml', 'twisted.web.resource',
                                'sqlalchemy.dialects.mssql', 'sqlalchemy.util',
                                'sqlalchemy.util.queue', 'pyodbc'
                                ],
                'packages': ['leftronicd.contrib', 'leftronicd.contrib.dbretriever',
                            ],
                'dist_dir': 'exe_dist',
                        }
            }
    #windows="leftronicd/main.py"
)
