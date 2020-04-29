#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path
from setuptools import find_packages, setup
from freebsd_sysctl.__version__ import VERSION
from changelogmd import Changelog


def _read_requirements(
    filename: str="requirements.txt"
) -> typing.Dict[str, typing.List[str]]:
    reqs = list(parse_requirements(filename, session="ioc_cli"))
    return dict(
        install_requires=list(map(lambda x: f"{x.name}{x.specifier}", reqs)),
        dependency_links=list(map(
            lambda x: str(x.link),
            filter(lambda x: x.link, reqs)
        ))
    )


_requirements = _read_requirements("requirements.txt")

with open(
    os.path.join(os.path.dirname(__file__), "README.md"),
    encoding="utf-8"
) as f:
    long_description = f.read()

setup(
    name="freebsd-sysctl",
    version=VERSION,
    description="Native Python wrapper for FreeBSD sysctls using libc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gronke/py-freebsd_sysctl",
    author="Stefan Grönke",
    author_email="stefan@gronke.net",
    python_requires=">=3.6",
    install_requires=_requirements["install_requires"],
    dependency_links=_requirements["dependency_links"],
    tests_require=["pytest-runner", "pytest"],
    packages=find_packages(exclude=('tests',))
)
