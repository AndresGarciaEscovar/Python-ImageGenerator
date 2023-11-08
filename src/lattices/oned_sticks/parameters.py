"""
    Contains the functions to validate the parameters for the one-dimensional
    sticks lattice.
"""

# ##############################################################################
# Imports
# ##############################################################################


# General


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_validate' Functions
# ------------------------------------------------------------------------------


def _validate_params_box(box: dict) -> None:
    """
        Validates that the box parameters are valid.

        :param box: The box parameters.

        :raise TypeError: If the box parameters are not the correct type.

        :raise ValueError: If the box parameter values are not valid.
    """
    # Check the position_top variable is a list of 2 positions.
    value = box["position_top"]

    if not isinstance(value, list):
        raise TypeError(
            f"The box parameter \"position_top\" must be a list. Current type: "
            f"{type(value)}."
        )

    if len(value) != 2:
        raise ValueError(
            f"The box parameter \"position_top\" must be a list of 2 "
            f"positions. Current length: {len(value)}."
        )

    if not all(isinstance(position, (int, float)) for position in value):
        raise TypeError(
            f"The box parameter \"position_top\" must be a list of 2 "
            f"positions, i.e., two real numbers. Types: "
            f"{[type(position) for position in value]}."
        )

    # Check the width and height variables are positive real numbers.
    for vtype in ("width", "height"):
        value = box[vtype]

        if not isinstance(value, (int, float)):
            raise TypeError(
                f"The box parameter \"{vtype}\" must be a real number. Current "
                f"type: {type(value)}."
            )

        if value <= 0:
            raise ValueError(
                f"The box parameter \"{vtype}\" must be a positive real "
                f"number, i.e. a real number greater than zero. Current value: "
                f"{value}."
            )


def _validate_params_box_label(box: dict, box_labels: dict) -> None:
    """
        Validates that the box label parameters are valid.

        :param box: The box parameters.

        :param box_labels: The box label parameters.

        :raise TypeError: If the box label parameters are not the correct type.

        :raise ValueError: If the box label parameter values are not valid.
    """
    # Check the width and height variables are positive real numbers.
    for vvalue in ("height", "width"):
        value = box_labels[vvalue]

        if not isinstance(value, (int, float)):
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
    # Check the parameters are lists of real numbers, of length 2.
    for vtype in ("offsets", "position_end", "position_start"):
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

        if not all(isinstance(entry, (int, float)) for entry in value):
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

    if not isinstance(value, (int, float)):
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

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'validate' Functions
# ------------------------------------------------------------------------------


def validate(configuration: dict) -> None:
    """
        Validates the configuration of the lattice parameters. The general
        structure of the dictionary has already been validated.

        :param configuration: The configuration of the lattice.
    """
    # Validate the configuration.
    _validate_params_box(configuration["box"])
    _validate_params_box_label(configuration["box"], configuration["box_label"])
    _validate_params_lattice(configuration["box"], configuration["lattice"])
