from setuptools import setup, find_packages
from pip.req import parse_requirements
import pip

install_reqs = reqs = [str(ir.req) for ir in parse_requirements('requirements.txt',
    session=pip.download.PipSession())]
dev_reqs = [str(ir.req) for ir in parse_requirements('requirements_dev.txt',
    session=pip.download.PipSession())]

setup(
    name='dl_data_validation_toolset',
    version='0.2.0',
    description="Data unit testing for validating deep learning data samples post-conversion.",
    long_description="""
    Data coming from the Kevlar framework needs to be validated post-conversion. This toolset provides
    the necessary constructs for creating unit tests and posting the results to HTML output.
    """,
    author="Kevin Wierman",
    author_email='kwierman@gmail.com',
    url='https://github.com/kwierman/dl_data_validation_toolset',
    packages=find_packages(),
    package_dir={'dl_data_validation_toolset': 'dl_data_validation_toolset'},
    entry_points={
        'console_scripts': ['ddvt=dl_data_validation_toolset.cli:main'],
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
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=dev_reqs
)
