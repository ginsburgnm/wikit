#!/usr/bin/env python
# setup script
from setuptools import setup
import versioneer

setup(
    version=versioneer.get_version(),
    install_requires=[
        'Wikipedia-API==0.5.4'
    ],
    cmdclass=versioneer.get_cmdclass(),
)
