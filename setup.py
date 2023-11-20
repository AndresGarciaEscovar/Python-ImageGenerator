"""
    File to setup the package.
"""

# ##############################################################################
# Imports
# ##############################################################################

# General
from setuptools import setup

# ##############################################################################
# parameters
# ##############################################################################


# List with required packages.
REQUIRED = [
    "numpy==1.26.2",
    "pyyaml==6.0.1",
]


# ##############################################################################
# Setup
# ##############################################################################


setup(
    author="Andres Garcia Escovar",
    author_email="andrumen@hotmail.com",
    description=(
        "Package that contains various functions to generate LaTeX code for "
        "several shapes."
    ),
    install_requires=REQUIRED,
    license="MIT",
    name="latex_lattices",
    package_dir={"": "latexlattices"},
    version="0.0.1",
)
