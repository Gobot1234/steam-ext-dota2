# -*- coding: utf-8 -*-

import re

from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    f.close()

with open("steam/ext/tf2/__init__.py") as f:
    search = re.search(r'^__version__\s*=\s*"([^"]*)"', f.read(), re.MULTILINE)

if search is None:
    raise RuntimeError("Version is not set")

version = search.group(1)

if version.endswith(("a", "b")) or "rc" in version:
    # try to find out the commit hash if checked out from git, and append
    # it to __version__ (since we use this value from setup.py, it gets
    # automatically propagated to an installed copy as well)
    try:
        import subprocess

        out = subprocess.getoutput("git rev-list --count HEAD")
        if out:
            version = f"{version}{out.strip()}"
        out = subprocess.getoutput("git rev-parse --short HEAD")
        if out:
            version = f"{version}+g{out.strip()}"
    except Exception:
        pass

with open("README.md") as f:
    readme = f.read()

setup(
    name="steam-ext-tf2",
    author="Gobot1234",
    url="https://github.com/Gobot1234/steam-ext-tf2",
    project_urls={
        "Issue tracker": "https://github.com/Gobot1234/steam-ext-tf2/issues",
    },
    version=version,
    packages=[
        "steam.ext.tf2",
    ],
    license="MIT",
    description="An extension for steam.py to interact with Team Fortress 2",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.7",
)
