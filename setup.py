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
    "numpy==1.26.0",
    "pyyaml==6.0",
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
    name="shapesLaTeX",
    package_dir={"": "src"},
    version="0.0.1",
)
