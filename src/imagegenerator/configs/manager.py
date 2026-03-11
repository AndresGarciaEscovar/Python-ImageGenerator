"""
    Contains the functions to handle the project's configurations.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from importlib.resources import files
from typing import Any

# User.
import imagegenerator.configs as configs


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Dictionary with the paths of the configurations.
_CONFIGS: dict = {
    "rsa_1d": files(configs).joinpath("rsa_1")
}


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _validate_name(name: Any) -> None:
    """
        Validates the name of the requested configuration.

        :param name: The name of the requested package.

        :raise KeyError: If the key does not exist.

        :raise TypeError: If the "name" variable is not a name.
    """
    # Check it is a string.
    if not isinstance(name, str):
        raise TypeError(
            f"The \"name\" parameter must be of type string; curren type is: "
            f"{type(name).__name__}."
        )

    # Check it exists in the dictionary.
    if name not in _CONFIGS:
        keys: str = ", ".join(
            f"\"{x}\""
            for x in sorted(_CONFIGS.keys(), key=lambda x: x.lower())
        )

        raise KeyError(
            f"The \"name\" (\"{name}\") does not exist in the dictionary; "
            f"valid keys are: {keys}."
        )


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def get_configuration(name: str) -> str:
    """
        Gets the path of the configuration.

        :param name: The name of the requested configuration.

        :return: A string with the path to the json file with the standard
         configuration for the requested model.
    """
    # Validate the name.
    _validate_name(name)

    return f"{_CONFIGS[name]}"
