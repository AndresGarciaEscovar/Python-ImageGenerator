"""
    File that contains the functions to generate the lattice LaTeX code.
"""


# ##############################################################################
# Imports
# ##############################################################################


# General
import yaml

from pathlib import Path

# User defined
from src.lattices.oned_sticks import parameters

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_get' Functions
# ------------------------------------------------------------------------------


def _get_configuration() -> dict:
    """
        Gets the configuration of the lattice.

        :return: The dictionary with the configuration of the lattice.
    """
    # Absolute path to the file.
    path = Path(__file__).parent.absolute() / "parameters.yaml"

    # Get the configuration.
    with open(f"{path}", mode="r") as file:
        configuration = yaml.safe_load(file)

    return configuration


# ------------------------------------------------------------------------------
# '_validate' Functions
# ------------------------------------------------------------------------------


def _validate_configuration(configuration: dict) -> dict:
    """
        Validates the configuration of the lattice.

        :param configuration: The configuration of the lattice.
    """
    # Get the valid configuration.
    vconfig = _get_configuration()

    # Change the values and check all keys are consistent.
    for key in configuration.keys():
        for key0, value0 in configuration[key].items():
            vconfig[key][key0] = value0

    # Validate the parameters.
    parameters.validate(vconfig)

    return vconfig

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'generate' Functions
# ------------------------------------------------------------------------------


def generate(configuration: dict = None) -> str:
    """
        Function that generates the lattice LaTeX code.

        :param configuration: The configuration of the lattice.

        :return: The lattice LaTeX code.
    """
    # Get the configuration.
    config = _get_configuration() if configuration is None else configuration
    config = _validate_configuration(config)

