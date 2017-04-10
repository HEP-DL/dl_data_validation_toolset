#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]

test_reqs = parse_requirements("requirements.txt")
test_reqs = [str(ir.req) for ir in test_reqs]

setup(
    name='dl_data_validation_toolset',
    version='0.1.0',
    description="Save the Kevin. Save the World.",
    long_description="TODO: Fill in",
    author="Kevin Wierman",
    author_email='kwierman@gmail.com',
    url='https://github.com/kwierman/dl_data_validation_toolset',
    packages=[
        'dl_data_validation_toolset',
    ],
    package_dir={'dl_data_validation_toolset':
                 'dl_data_validation_toolset'},
    entry_points={
        'console_scripts': [
            'dl_data_validation_toolset=dl_data_validation_toolset.cli:main'
        ],
    },
    include_package_data=True,
    install_requires=reqs,
    license="MIT license",
    zip_safe=False,
    keywords='dl_data_validation_toolset',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_reqs
)