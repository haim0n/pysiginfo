#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


requirements = [
    'psutil>=5.9.0',
]

setup(
    name='pysiginfo',
    version='1.0.0',
    description='Process signals info utility',
    long_description='\n\n',
    author='Haim Daniel',
    url='https://github.com/haim0n/pysiginfo.git',
    packages=[
       'pysiginfo',
    ],
    package_dir={'pysiginfo': 'pysiginfo'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords=['signals', 'python'],
    entry_points={
        'console_scripts': [
            'siginfo = pysiginfo.siginfo:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
