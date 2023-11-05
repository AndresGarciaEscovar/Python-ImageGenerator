"""
    File that contains the basic parameters for the one dimensional sticks
    lattice. Default values will be given with respect to the total page
    width = 15cm.
"""


# ##############################################################################
# Imports
# ##############################################################################


# General.
import yaml

from pathlib import Path


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Units
# ##############################################################################


# Basic units are centimeters.
_UNITS = "cm"


# ##############################################################################
# Global Variables
# ##############################################################################


# Main box parameters.
_MAIN_BOX = {
    "width": 15.0,
    "height": 15.0,
    "margin-bottom": 0.5,
    "margin-left": 0.5,
    "margin-right": 0.5,
    "margin-top": 0.5,
    "label-height": 2.0,
    "label-width": 2.0,
    "label-postion": {"x": 0, "y": 0},
}

# Line elements.
_LINES = {
    "arrow-height": 2.0,
    "base-width": 14.0,
    "base-position-x": 0.5,
    "base-position-y": -7.5,
    "tick-height": 2.0,
    "tick-offset-x-left": 0,
    "tick-offset-x-right": 0,
    "tick-offset-y-bottom": 0,
    "tick-offset-y-top": 0,
}

# Particle.
_PARTICLES = {
    "circle-radius": 1.0,
    "nticks": 1,
    "padsorb": [],
    "pdesorb": [],
    "pfixed": [],
    "pjumps": [],
    "ptype": "circle",
    "vacancy-show": False,
}


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_get' Functions
# ------------------------------------------------------------------------------


def _get_path_unique(path: Path, name: str) -> str:
    """
        If the file requested already exists, a new file name will be generated
        by adding a number at the end of the file name.

        :param path: The path to the file.

        :return: The string with the path to the file with a unique name.
    """
    # Auxiliary variables.
    tpath = path / f"{name}.yaml"

    # Check if the file exists.
    counter = 0
    while tpath.is_file():
        tpath = path / f"{name}_({counter}).yaml"
        counter += 1

    return f"{tpath}"


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'create' Functions
# ------------------------------------------------------------------------------


def create_configuration(path: str) -> None:
    """
        Creates a yaml configuration file for the one dimensional sticks
        lattice in the given location.

        :param path: The path where the configuration file will be created.
    """
    # Get the configuration parameters.
    _, parameters = get_parameters()
    del _

    # Path to the directory where the file will be saved.
    tpath = Path(path)

    # A valid path must be given.
    if not tpath.is_dir():
        raise ValueError(
            f"The path must be a directory. Current path: \"{tpath}\"."
        )

    # Create the file with a unique name.
    tpath = _get_path_unique(tpath, "oned_sticks_config")
    with open(tpath, "w") as file:
        yaml.dump(parameters, file)


# ------------------------------------------------------------------------------
# 'get' Functions
# ------------------------------------------------------------------------------


def get_parameters() -> tuple:
    """
        Returns the units and the customizable parameters for the lattice. The
        first element of the tuple is the units and the second element is a
        dictionary with the parameters.

        :return: The units and the customizable parameters for the lattice.
    """
    return _UNITS, {
        "main-box": _MAIN_BOX,
        "lines": _LINES,
        "particles": _PARTICLES,
        "units": _UNITS,
    }
