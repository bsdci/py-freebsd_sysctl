#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path
from freebsd_sysctl.__version__ import __version__
from setuptools import find_packages, setup
from distutils.command.build_py import build_py
from distutils.command.sdist import sdist
import distutils.log


class BuildCommand(build_py):

    def run(self):
        super().run()

        self.announce(
            f"Tagging version {__version__}",
            level=distutils.log.INFO
        )
        if not self.dry_run:
            # generate .version files
            for package in self.distribution.packages:
                target = os.path.join(
                    self.build_lib,
                    package,
                    ".version"
                )
                with open(target, "w", encoding="UTF-8") as f:
                    f.write(__version__)
                    f.truncate()


class SdistCommand(sdist):

    def run(self):
        self.announce(
            f"Bundling Source Distribution of Release {__version__}",
            level=distutils.log.INFO
        )
        created_release_files = set()

        if not self.dry_run:
            # generate temporary RELEASE files
            for package in self.distribution.packages:
                release_file = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    package,
                    ".version"
                )
                if os.path.isfile(release_file) is False:
                    created_release_files.add(release_file)
                    with open(release_file, "w", encoding="UTF-8") as f:
                        f.write(__version__)
                        f.truncate()
        try:
            pass
            super().run()
        finally:
            if not self.dry_run:
                for release_file in created_release_files:
                    os.remove(release_file)


with open(
    os.path.join(os.path.dirname(__file__), "README.md"),
    encoding="utf-8"
) as f:
    long_description = f.read()

packages = find_packages(exclude=('tests',))
    name="freebsd-sysctl",
    version=__version__,
    description="Native Python wrapper for FreeBSD sysctls using libc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gronke/py-freebsd_sysctl",
    author="Stefan Grönke",
    author_email="stefan@gronke.net",
    python_requires=">=3.6",
    tests_require=["pytest-runner", "pytest"],
    include_package_data=True,
    packages=packages,
    provides=packages,
    cmdclass=dict(
        build_py=BuildCommand,
        sdist=SdistCommand
    )
)
