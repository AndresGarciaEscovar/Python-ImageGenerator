"""
    Contains the functions to validate the parameters for the one-dimensional
    sticks lattice.
"""

# ##############################################################################
# Imports
# ##############################################################################


# General
import yaml

from importlib.resources import files
from typing import Any

# User defined
import src.lattices.oned_sticks as src


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Dictionary structure with the keys and types of the parameters.
_TEMPLATE = {
    "box": {
      "position_top": list,
      "height": (float, int),
      "width": (float, int),
    },
    "box_label": {
      "height": (float, int),
      "width": (float, int),
    },
    "lattice": {
      "offsets": list,
      "position_end": list,
      "position_start": list,
      "vertical_spacing": (float, int),
    },
    "lattice_elements": {
      "arrow_height": (float, int),
      "circle_radius": (float, int),
      "tick_height": (float, int),
      "vacancies_visible": bool
    },
    "lattice_parameters": {
      "nticks": int,
      "adsorbing": list,
      "desorbing": list,
      "fixed": list,
      "jumping": list,
    }
}


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_validate' Functions
# ------------------------------------------------------------------------------

def _validate_general(dictionary: Any) -> None:
    """
        Validates the general structure of the dictionary.

        :param dictionary: The object to be validated.

        :raise TypeError: If the entries in the dictionary are not the correct
         type.

        :raise ValueError: If the values of the dictionary are not valid.
    """
    # Global variables.
    global _TEMPLATE

    # Must be a dictionary.
    if not isinstance(dictionary, dict):
        raise TypeError(
            f"The object being validated must be a dictionary. Current type: "
            f"{type(dictionary)}."
        )

    # Keys of the dictionary.
    keys = set(_TEMPLATE.keys())
    if keys != set(dictionary.keys()):
        raise ValueError(
            f"The first level of the dictionary must have the following keys: "
            f"{keys}. Current keys: {set(dictionary.keys())}."
        )

    # Validate the entries of the dictionary.
    for key, value in dictionary.items():
        # Check they are dictionaries.
        if not isinstance(value, dict):
            raise TypeError(
                f"The entries of the dictionary must be dictionaries. Current "
                f"type: {type(value)}."
            )

        # Check the keys of the dictionary.
        if set(value.keys()) != set(_TEMPLATE[key].keys()):
            raise ValueError(
                f"The second level of the dictionary with key \"{key}\" must "
                f"have the following keys: {set(_TEMPLATE[key].keys())}. "
                f"Current keys: {set(value.keys())}."
            )

        # Check the types of the values of the dictionary.
        for key0, value0 in value.items():
            if not isinstance(value0, _TEMPLATE[key][key0]):
                raise TypeError(
                    f"The value of the entry with key \"{key0}\" of the "
                    f"dictionary with key \"{key}\" must be of type "
                    f"{_TEMPLATE[key][key0]}. Current type: {type(value0)}."
                )


def _validate_params_box(box: dict) -> None:
    """
        Validates that the box parameters are valid.

        :param box: The box parameters.

        :raise TypeError: If the box parameters are not the correct type.

        :raise ValueError: If the box parameter values are not valid.
    """
    # Dictionary with the keys and types of the parameters.
    box = {
        "position_top": list,
        "height": (float, int),
        "width": (float, int),
    }


def _validate_params_box_label(box: dict, box_labels: dict) -> None:
    """
        Validates that the box label parameters are valid.

        :param box: The box parameters.

        :param box_labels: The box label parameters.

        :raise TypeError: If the box label parameters are not the correct type.

        :raise ValueError: If the box label parameter values are not valid.
    """
    # Keys.
    keys = {"height", "width"}
    if set(box_labels.keys()) != keys:
        raise ValueError(
            f"The box_label parameters must have the following keys: {keys}. "
            f"Current keys: {set(box_labels.keys())}."
        )

    # Check the width and height variables are positive real numbers.
    for vvalue in keys:
        value = box_labels[vvalue]

        if not isinstance(value, (float, int)):
            raise TypeError(
                f"The box_label parameter \"{vvalue}\" must be a real number. "
                f"Current type: {type(value)}."
            )

        if value <= 0:
            raise ValueError(
                f"The box_label parameter \"{vvalue}\" must be a positive real "
                f"number, i.e. a real number greater than zero. Current value: "
                f"{value}."
            )

        if value > box[vvalue]:
            raise ValueError(
                f"The box_label parameter \"{vvalue}\" must be less than or "
                f"equal to the box parameter \"height\". Current values: "
                f"{value}, {box[vvalue]}."
            )


def _validate_params_lattice(box: dict, lattice: dict) -> None:
    """
        Validates that the lattice parameters are valid.

        :param box: The box parameters.

        :param lattice: The lattice parameters.

        :raise TypeError: If the lattice parameters are not the correct type.

        :raise ValueError: If the lattice parameters values are not valid.
    """
    # Keys.
    keys = {"offsets", "position_end", "position_start", "vertical_spacing"}
    if set(lattice.keys()) != keys:
        raise ValueError(
            f"The lattice parameters must have the following keys: {keys}. "
            f"Current keys: {set(lattice.keys())}."
        )

    # Check the parameters are lists of real numbers, of length 2.
    for vtype in {"offsets", "position_end", "position_start"}:
        value = lattice[vtype]

        if not isinstance(value, list):
            raise TypeError(
                f"The lattice parameter \"{vtype}\" must be a list. Current "
                f"type: {type(value)}."
            )

        if len(value) != 2:
            raise ValueError(
                f"The lattice parameter \"{vtype}\" must be a list of 2 "
                f"entries. Current length: {len(value)}."
            )

        if not all(isinstance(entry, (float, int)) for entry in value):
            raise TypeError(
                f"The lattice parameter \"{vtype}\" must be a list of 2 "
                f"entries, i.e., two real numbers. Types: "
                f"{[type(entry) for entry in value]}."
            )

        if not all(entry >= 0 for entry in value):
            raise ValueError(
                f"The lattice parameter \"{vtype}\" must be a list of 2 "
                f"positive valued entries. Current values: "
                f"{value}."
            )

    # Check that the vertical spacing is a positive real number.
    value = lattice["vertical_spacing"]

    if not isinstance(value, (float, int)):
        raise TypeError(
            f"The lattice parameter \"vertical_spacing\" must be a real "
            f"number. Current type: {type(value)}."
        )

    if value <= 0:
        raise ValueError(
            f"The lattice parameter \"vertical_spacing\" must be a positive "
            f"real number, i.e. a real number greater than zero. Current "
            f"value: {value}."
        )

    # ------------------- Validate the position parameters ------------------- #

    # Ge the positions.
    pstr = lattice["position_start"]
    pend = lattice["position_end"]

    if not (0 <= pstr[0] < pend[0] <= box["width"]):
        raise ValueError(
            f"The position of the x values of the positions of the lattice "
            f"base are not in a valid range. The valid order is: "
            f"0 <= \"position_start[0]\" < \"position_end[0]\" <= "
            f"\"box[\'width\']\". Current values are: \"position_start[0]\" = "
            f"{pstr[0]}, \"position_end[0]\" = {pend[0]} and "
            f"\"box[\'width\']\" = {box['width']}."
        )

    if not (0 <= pstr[1] == pend[1] <= box["height"]):
        raise ValueError(
            f"The position of the y values of the positions of the lattice "
            f"base must be equal and less than the height of the lattice. "
            f"Current values are: \"position_start[1]\" = "
            f"{pstr[1]}, \"position_end[1]\" = {pend[1]} and "
            f"\"box[\'height\']\" = {box['height']}."
        )

    # ------------ Validate offsets with respect to start and end ------------ #

    offset_l = lattice["offsets"][0]
    offset_r = lattice["offsets"][1]

    if (apos := pstr[0] + offset_l) >= (bpos := pend[0] - offset_r):
        raise ValueError(
            f"The position of the left offset exceeds or is the same as that "
            f"of the right offset. That is, {apos:.5f} >= {bpos:.5f}; where "
            f"offset_l is \"pstr[0] + lattice['offsets'][0]\" and offset_r is "
            f"\"pend[0] - lattice['offsets'][1]\"."
        )


def _validate_params_lattice_elements(elements: dict) -> None:
    """
        Validates that the lattice elements are consistent with the lattice
        parameters.

        :param elements: The lattice elements.

        :raise TypeError: If the lattice elements are not the correct type.

        :raise ValueError: If the lattice elements don't have correct values.
    """
    # Keys.
    keys = {"arrow_height", "circle_radius", "tick_height", "vacancies_visible"}
    if set(elements.keys()) != keys:
        raise ValueError(
            f"The lattice elements must have the following keys: {keys}. "
            f"Current keys: {set(elements.keys())}."
        )

    # Validate all the elements.
    for vtype in keys:
        # Variable value.
        value = elements[vtype]

        # Validate the value is a boolean value.
        if vtype == "vacancies_visible":
            if not isinstance(value, bool):
                raise TypeError(
                    f"The lattice element \"{vtype}\" must be a boolean. "
                    f"Current type: {type(value)}."
                )
            continue

        # Validate the value is a positive real number.
        if not isinstance(value, (float, int)):
            raise TypeError(
                f"The lattice element \"{vtype}\" must be a real number. "
                f"Current type: {type(value)}."
            )

        if value <= 0:
            raise ValueError(
                f"The lattice element \"{vtype}\" must be a positive real "
                f"number, i.e. a real number greater than zero. Current value: "
                f"{value}."
            )


def validate_params_lattice_parameters(parameters: dict,) -> None:
    """
        Validates the parameters of the lattice, i.e., the parameters that
        define the position of the elements of the particles.

        :param parameters: The parameters of the lattice.

        :raise TypeError: If the parameters are not the correct type.

        :raise ValueError: If the parameters don't have correct values.
    """
    # Keys.
    keys = {"nticks", "adsorbing", "desorbing", "fixed", "jumping"}
    if set(parameters.keys()) != keys:
        raise ValueError(
            f"The lattice parameters must have the following keys: {keys}. "
            f"Current keys: {set(parameters.keys())}."
        )


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'get' Functions
# ------------------------------------------------------------------------------


def get() -> dict:
    """
        Gets the dictionary with the default parameters.

        :return: The dictionary with the default parameters.
    """
    with files(src.__name__).joinpath("parameters.yaml").open() as file:
        return yaml.safe_load(file)

# ------------------------------------------------------------------------------
# 'validate' Functions
# ------------------------------------------------------------------------------


def validate(configuration: dict) -> None:
    """
        Validates the configuration of the lattice parameters. The general
        structure of the dictionary has already been validated.

        :param configuration: The configuration of the lattice.
    """
    # Validate general parameters.
    _validate_general(configuration)

    # Validate the configuration.
    _validate_params_box(configuration["box"])
    # _validate_params_box_label(configuration["box"], configuration["box_label"])
    # _validate_params_lattice(configuration["box"], configuration["lattice"])
    # _validate_params_lattice_elements(configuration["lattice_elements"])

