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
import latexlattices.lattices.oned_sticks as src
import latexlattices.validate.validate_properties as vproperties


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
        "nmers": int,
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
    kargs = {
        "position_top": {
            "value": box["position_top"],
            "dtype": (int, float),
            "length": 2,
            "name": "box[\"position_top\"]",
            "texcept": True
        },
        "height": {
            "value": box["height"],
            "zero": False,
            "name": "box[\"height\"]",
            "texcept": True
        },
        "width": {
            "value": box["width"],
            "zero": False,
            "name": "box[\"width\"]",
            "texcept": True
        },
    }

    # Validate the parameters.
    vproperties.validate_list(**kargs["position_top"])
    vproperties.validate_real_positive(**kargs["height"])
    vproperties.validate_real_positive(**kargs["width"])


def _validate_params_box_label(box: dict, box_labels: dict) -> None:
    """
        Validates that the box label parameters are valid.

        :param box: The box parameters.

        :param box_labels: The box label parameters.

        :raise TypeError: If the box label parameters are not the correct type.

        :raise ValueError: If the box label parameter values are not valid.
    """
    # Dictionary with the keys and types of the parameters.
    kargs = {
        "height": {
            "value": box_labels["height"],
            "zero": True,
            "name": "box_labels[\"height\"]",
            "texcept": True
        },
        "width": {
            "value": box_labels["width"],
            "zero": True,
            "name": "box_labels[\"width\"]",
            "texcept": True
        },
    }

    # Validate the parameter values.
    vproperties.validate_real_positive(**kargs["height"])
    vproperties.validate_real_positive(**kargs["width"])

    # Check the box label fits in the box.
    if box_labels["height"] > box["height"]:
        raise ValueError(
            f"The height of the label box must be less than or equal to the "
            f"height of the box. Current values: {box['height'] = }, "
            f"{box_labels['height'] = }."
        )

    if box_labels["width"] > box["width"]:
        raise ValueError(
            f"The width of the label box must be less than or equal to the "
            f"width of the box. Current values: {box['width'] = }, "
            f"{box_labels['width'] = }."
        )


def _validate_params_lattice(box: dict, lattice: dict) -> None:
    """
        Validates that the lattice parameters are valid.

        :param box: The box parameters.

        :param lattice: The lattice parameters.

        :raise TypeError: If the lattice parameters are not the correct type.

        :raise ValueError: If the lattice parameters values are not valid.
    """
    # Dictionary with the keys and types of the parameters.
    kargs = {
        "offsets": {
            "value": lattice["offsets"],
            "dtype": (int, float),
            "length": 2,
            "name": "lattice[\"offsets\"]",
            "texcept": True
        },
        "position_end": {
            "value": lattice["position_end"],
            "dtype": (int, float),
            "length": 2,
            "name": "lattice[\"position_end\"]",
            "texcept": True
        },
        "position_start": {
            "value": lattice["position_start"],
            "dtype": (int, float),
            "length": 2,
            "name": "lattice[\"position_start\"]",
            "texcept": True
        },
        "vertical_spacing": {
            "value": lattice["vertical_spacing"],
            "zero": False,
            "name": "lattice[\"vertical_spacing\"]",
            "texcept": True
        },
    }

    # General validation.
    vproperties.validate_list(**kargs["offsets"])
    vproperties.validate_list(**kargs["position_end"])
    vproperties.validate_list(**kargs["position_start"])
    vproperties.validate_real_positive(**kargs["vertical_spacing"])

    # -------------------- Must have positive real numbers ------------------- #

    # All numbers must be real and, possibly, zero.
    falias = vproperties.validate_real_positive
    for key in {"offsets", "position_end", "position_start"}:
        kargs = {
            "zero": True,
            "texcept": False,
        }

        if not all(falias(value=x, **kargs) for x in lattice[key]):
            raise ValueError(
                f"The values of the lattice parameter \"{key}\" must be "
                f"positive real numbers. Current values: {lattice[key]}."
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
    # Dictionary with the keys and types of the parameters.
    kargs = {
        "arrow_height": {
            "value": elements["arrow_height"],
            "zero": False,
            "name": "elements[\"arrow_height\"]",
            "texcept": True
        },
        "circle_radius": {
            "value": elements["circle_radius"],
            "zero": False,
            "name": "elements[\"circle_radius\"]",
            "texcept": True
        },
        "tick_height": {
            "value": elements["tick_height"],
            "zero": False,
            "name": "elements[\"tick_height\"]",
            "texcept": True
        },
        "vacancies_visible": {
            "value": elements["vacancies_visible"],
            "name": "elements[\"vacancies_visible\"]",
            "texcept": True
        },
    }

    # Validate the parameters.
    vproperties.validate_real_positive(**kargs["arrow_height"])
    vproperties.validate_real_positive(**kargs["circle_radius"])
    vproperties.validate_real_positive(**kargs["tick_height"])
    vproperties.validate_bool(**kargs["vacancies_visible"])


def _validate_params_lattice_parameters(parameters: dict,) -> None:
    """
        Validates the parameters of the lattice, i.e., the parameters that
        define the position of the elements of the particles.

        :param parameters: The parameters of the lattice.

        :raise TypeError: If the parameters are not the correct type.

        :raise ValueError: If the parameters don't have correct values.
    """
    # Dictionary with the keys and types of the parameters.
    kargs = {
        "nmers": {
            "value": parameters["nmers"],
            "zero": False,
            "name": "lattice_parameters[\"nmers\"]",
            "texcept": True
        },
        "nticks": {
            "value": parameters["nticks"],
            "zero": False,
            "name": "lattice_parameters[\"nticks\"]",
            "texcept": True
        },
        "adsorbing": {
            "value": parameters["adsorbing"],
            "dtype": int,
            "name": "lattice_parameters[\"adsorbing\"]",
            "texcept": True
        },
        "desorbing": {
            "value": parameters["desorbing"],
            "dtype": int,
            "name": "lattice_parameters[\"desorbing\"]",
            "texcept": True
        },
        "fixed": {
            "value": parameters["fixed"],
            "dtype": int,
            "name": "lattice_parameters[\"fixed\"]",
            "texcept": True
        },
        "jumping": {
            "value": parameters["jumping"],
            "dtype": Any,
            "name": "lattice_parameters[\"jumping\"]",
            "texcept": True
        },
    }

    # Validate the parameters.
    vproperties.validate_int_positive(**kargs["nmers"])
    vproperties.validate_int_positive(**kargs["nticks"])
    vproperties.validate_list(**kargs["adsorbing"])
    vproperties.validate_list(**kargs["desorbing"])
    vproperties.validate_list(**kargs["fixed"])
    vproperties.validate_list(**kargs["jumping"])

    # N-mers must be less than or equal to the number of ticks.
    if parameters["nmers"] > parameters["nticks"]:
        raise ValueError(
            f"The number of ticks must be greater than or equal to the "
            f"number of n-mers. Current values: {parameters['nticks'] = }, "
            f"{parameters['nmers'] = }."
        )

    # The adsorbing, desorbing and fixed lists must be between 0 and nticks.
    for key in {"adsorbing", "desorbing", "fixed"}:
        # No need to check.
        if len(parameters[key]) == 0:
            continue

        # Exceptions must be raised.
        threshold = parameters['nticks'] - (parameters["nmers"] - 1)
        if not all(0 <= x < parameters["nticks"] for x in parameters[key]):
            raise ValueError(
                f"The values of the lattice parameter \"{key}\" must be in the "
                f"lattice, i.e., between 0 and {threshold}. Current values: "
                f"{parameters[key]}."
            )

        # Arrays must have unique elements.
        if len(set(parameters[key])) != len(parameters[key]):
            raise ValueError(
                f"The values of the lattice parameter \"{key}\" must be unique. "
                f"Current values: {parameters[key]}."
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
    _validate_params_box_label(configuration["box"], configuration["box_label"])
    _validate_params_lattice(configuration["box"], configuration["lattice"])
    _validate_params_lattice_elements(configuration["lattice_elements"])
    _validate_params_lattice_parameters(configuration["lattice_parameters"])
