# -*- coding: utf-8 -*-

import setuptools
from pathlib import Path

root = Path(__file__).parent
long_description = (root / "README.md").read_text(encoding="utf-8")
package_metadata = {}
exec((root / "versionwarning" / "__init__.py").read_text(encoding="utf-8"), package_metadata)

setuptools.setup(
    name="sphinxext-versionwarning",
    version=package_metadata["version"],
    author="Manuel Kaufmann, Graham Howard",
    author_email="sphinx@grahamsh.com",
    description="Sphinx extension to add a warning banner",
    url="https://github.com/grahamsh-llk/sphinx-version-warning",
    packages=setuptools.find_packages(),
    package_data={"versionwarning": ["_static/js/versionwarning.js"]},
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=False,
    zip_safe=False,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        "sphinx",
    ],
)
