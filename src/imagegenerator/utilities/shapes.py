"""
    File that contains the functions to generate the different shapes.
"""
# pylint: disable=too-many-arguments,too-many-positional-arguments

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Callable

# User.
import imagegenerator.validate.shapes as vshapes


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _get_formatted_color(color: tuple) -> str:
    """
        Formats the color based on the color tuple.

        :param color: The color 4-tuple that contains the proper entries.

        :return: A string with the formatted prefix to the string.
    """
    # Auxiliary variables.
    prefix = "\\draw[" if color[2] is None else "\\filldraw["
    options: tuple = ("opacity", "draw", "fill", "line width")
    dictionary: dict = dict(zip(options, color))

    # Format the keys.
    for key, value in dictionary.items():
        if value is not None:
            prefix += f"{key}={value}, "

    return prefix.strip().strip(",") + "] "


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def get_circle(
    radius: float = 1.0,
    position: tuple = (0, 0),
    units: str = "cm",
    color: tuple = ("1.0", "red", "blue", "0.4pt")
) -> str:
    """
        Gets the code for a circle.

        :param radius: A floating point number that represents the radius of
         a circle. It must be a positive numbers greater than zero.

        :param position: A tuple that represents the position of the middle of
         the circle.

        :param units: A string with the intended units.

        :param color: A tuple indicating the color of the circle, where the
         first entry represents the opacity, the second entry the color of the
         outline, the third entry represents the color of the fill, and the
         last entry represents the thickness of the outline. If one of the
         values is not used, the default value for it is used.

        :return: A string with the TikZ code for a circle.
    """
    return get_ellipse((radius, radius), position, units, color)


def get_coordinate(coordinate: tuple, units: str = "cm") -> str:
    """
        From the given coordinate, gets the string representation of the value.

        :param coordinate: The coordinate to be converted into a string.

        :return: A string representing the coordinate.
    """
    # Validate the coordinate.
    vshapes.validate_coordinate(coordinate)

    return f"({', '.join(f'{float(x):+.4f}{units}' for x in coordinate)})"


def get_ellipse(
    radius: tuple = (1.0, 1.0),
    position: tuple = (0, 0),
    units: str = "cm",
    color: tuple = ("1.0", "red", "blue", "0.4pt")
) -> str:
    """
        Gets the code for an ellipse.

        :param radius: A tuple with the semi-major and semi-minor axis lengths.
         If the axis are the same, they form a circle. They must both be
         positive numbers greater than zero.

        :param position: A tuple that represents the position of the middle of
         the ellipse.

        :param units: A string with the intended units.

        :param color: A tuple indicating the color of the ellipse, where the
         first entry represents the opacity, the second entry the color of the
         outline, the third entry represents the color of the fill, and the
         last entry represents the thickness of the outline. If one of the
         values is not used, the default value for it is used.

        :return: A string with the TikZ code for a simple ellipse.
    """
    # Auxiliary variables.
    function: Callable = lambda x: get_coordinate(x, units)

    # Get the coordinates.
    ctr: str = function(position)

    # Dictionary from the keys.
    string: str = f"{ctr} ellipse ({radius[0]}{units} and {radius[1]}{units})"

    # Setup the color.
    prefix: str = _get_formatted_color(color)

    return f"{prefix}{string};"


def get_rectangle(
    length: float = 1.0,
    width: float = 1.0,
    position: tuple = (0, 0),
    units: str = "cm",
    color: tuple = ("1.0", None, None, "0.4pt")
) -> str:
    """
        Gets the code for a simple rectangle.

        :param length: The length of the box; must be a positive real number
         greater than zero.

        :param width: The width of the box; must be a positive real number
         greater than zero.

        :param position: A tuple that represents the position of the middle of
         the box.

        :param units: A string with the intended units.

        :param color: A tuple indicating the color of the rectangle, where the
         first entry represents the opacity, the second entry the color of the
         outline, the third entry represents the color of the fill, and the
         last entry represents the thickness of the outline. If one of the
         values is not used, the default value for it is used.

        :return: A string with the TikZ code for a simple rectangle.
    """
    # Auxiliary variables.
    function: Callable = lambda x: get_coordinate(x, units)

    # Get the coordinates.
    corners: tuple = (
        (-length / 2.0 + position[0], -width / 2.0 + position[1]),
        (+length / 2.0 + position[0], +width / 2.0 + position[1]),
    )

    # Dictionary from the keys.
    string: str = ' rectangle '.join(function(x) for x in corners)

    # Setup the color.
    prefix: str = _get_formatted_color(color)

    return f"{prefix}{string};"


def get_tick(
    base: float = 0.5,
    vertical: float = 1.0,
    position: tuple = (0, 0),
    offset: tuple = (0, 0),
    units: str = "cm",
    color: str = "black"
) -> str:
    """
        Gets the code for a tick.

        :param base: The base of the tick; must be a positive real number
         greater than zero.

        :param vertical: The length of the vertical part of the tick; must be
         a positive real number greater than zero.

        :param position: A tuple that represents the position of the middle of
         point of the base along the base.

        :param offset: The horizontal and vertical offset of the lower part of
         the tick with respect to the horizontal middle of the base (along the
         x-axis), and above the base (along the y-axis). Negative numbers
         represent left/right and top/bottom.

        :param units: A string with the intended units.

        :return: A string with the TikZ code for a simple tick.
    """
    # Auxiliary variables.
    function: Callable = lambda x: get_coordinate(x, units)

    # Get the coordinates.
    positions_base: tuple = (
        (-base / 2.0 + position[0], position[1]),
        (+base / 2.0 + position[0], position[1]),
    )
    positions_vertical: tuple = (
        (position[0] + offset[0], position[1] + offset[1]),
        (position[0] + offset[0], position[1] + offset[1] + vertical),
    )

    positions_base = tuple(function(x) for x in positions_base)
    positions_vertical = tuple(function(x) for x in positions_vertical)

    return (
        f"\\draw[color={color}] {' -- '.join(positions_base)};\n"
        f"\\draw[color={color}] {' -- '.join(positions_vertical)};"
    )


# #############################################################################
# TO DELETE
# #############################################################################


def run() -> None:
    """
        Runs the main code.
    """
    print(get_tick())


# -----------------------------------------------------------------------------
# Main Program
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    run()
