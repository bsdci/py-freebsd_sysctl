#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path
from setuptools import find_packages, setup


def read_first_line(relative_filename: str) -> str:
    absolute_path = os.path.join(os.getcwd(), relative_filename)
    with open(absolute_path, "r", encoding="UTF-8") as f:
        return f.readline().strip()


try:
    VERSION = read_first_line("VERSION")
except:
    # last git commit SHA is the version
    line = read_first_line(".git/HEAD")
    if line.startswith("ref: ") is False:
        VERSION = line
    else:
        ref = line[5:]
        VERSION = read_first_line(f".git/{ref}")


with open(os.path.join(cwd, "README.md"), encoding="utf-8") as f:
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
    tests_require=["pytest-runner", "pytest"],
    packages=find_packages(exclude=('tests',))
)
