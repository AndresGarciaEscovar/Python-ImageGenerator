"""
    File that contains the functions for the validation of 1 dimensional
    lattices, in this case, of 1D numpy arrays.
"""

# ##############################################################################
# Imports
# ##############################################################################


# General.
import numpy as np

from typing import Any


# ##############################################################################
# Global Variables
# ##############################################################################

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_validate' Functions
# ------------------------------------------------------------------------------


def _validate_shape(shape: Any) -> None:
    """
        Validates that the given parameters is a tuple of length 2 with positive
        non-zero integers.

        :param shape: The object to validate.

        :raise TypeError: If the object is not a tuple. If the object is not
         a tuple of length 2. If the object is not a tuple of positive non-zero
         integers.
    """
    # Validate the shape is a tuple.
    if not isinstance(shape, tuple):
        raise TypeError(
            f"The shape of the numpy array is not a tuple. Current type: "
            f"{type(shape)}."
        )

    # Check it has length 2.
    if len(shape) != 2:
        raise TypeError(
            f"The shape of the numpy array is not a tuple of length 2. Current "
            f"length: {len(shape)}."
        )

    # Check the elements are positive non-zero integers.
    if not all(isinstance(x, int) and x > 0 for x in shape):
        raise TypeError(
            f"The shape of the numpy array is not a tuple of positive non-zero "
            f"integers. Current shape: {shape}."
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


def validate_ndarray(array: Any, texcept: bool = True) -> bool:
    """
        Function that validates that the array object is a two dimensional numpy
        array.

        :param array: The object to validate.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the object is not a two dimensional numpy array. True, if an
         exception should be raised; False, otherwise. True, by default.

        :return: True, if the input is a two dimensional numpy array; False,
         otherwise.

        :raises TypeError: If the object is not a two dimensional numpy array
         and texcept is True.
    """
    # Check that the object a numpy array.
    flag = isinstance(array, np.ndarray)
    if not flag and texcept:
        raise TypeError(
            f"The array is not a numpy array. Current type: {type(array)}"
        )

    # Check that the object is a 2D numpy array.
    flag = flag and array.ndim == 2
    if not flag and texcept:
        raise ValueError(
            f"The array is not a two dimensional array. Current shape: "
            f"{array.shape}."
        )

    return flag


def validate_shape(array: Any, shape: tuple, texcept: bool = True) -> bool:
    """
        Function that validates that the array object is a numpy array of the
        specified shape.

        :param array: The array to validate.

        :param shape: The 2-entry tuple that specifies the shape of the array.

        :param texcept: If an exception must be thrown if the array is not of
         the specified shape. True, if an exception should be raised; False,
         otherwise. True, by default.

        :return: True, if the array is of the specified shape; False, otherwise.
    """
    # Check that the shape parameter is valid.
    _validate_shape(shape)

    # Validate it is a 2D numpy array.
    if not (flag := validate_ndarray(array, texcept=texcept)):
        return flag

    # Validate the length of the array.
    flag = array.shape == shape
    if not flag and texcept:
        raise ValueError(
            f"The array is not a two dimensional array of the specified "
            f"length. Current shape: {array.shape}, expected shape: {shape}."
        )

    return flag


def validate_type(array: Any, dtype: Any, texcept: bool = True) -> bool:
    """
        Function that validates that the array object is a numpy array of a
        the given type(s).

        :param array: The array to validate.

        :param dtype: The type of the elements of the array.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the object is not a numpy array of the specified type. True,
         if an exception should be raised; False, otherwise. True, by default.

        :return: True, if the object is a numpy array of the specified type;
         False, otherwise.

        :raises TypeError: If the object is not a numpy array of the specified
         type and texcept is True.
    """
    # Validate it is a 2D numpy array.
    if not (flag := validate_ndarray(array, texcept=texcept)):
        return flag

    # Validate the type of the elements.
    flag = array.dtype == dtype
    if not flag and texcept:
        raise TypeError(
            f"The array is not a numpy array of type {dtype}. Current type: "
            f"{array.dtype}."
        )

    return flag


def validate_type_negative(
    array: Any, dtype: Any, zero: bool = False, texcept: bool = True
) -> bool:
    """
        Function that validates that the array object is a numpy array of a
        given type(s) and ALL its elements are negative. If the zero option
        is set to True, then the value can be zero.

        :param array: The array to validate.

        :param dtype: The type of the elements of the array.

        :param zero: A boolean flag that indicates if the value of the array
         elements can be zero.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the object is not a numpy array of the specified type and all
         its values are negative or zero. The latter depends on the value of the
         zero option. True, if an exception should be raised; False, otherwise.
         True, by default.

        :return: True, if the object is a numpy array of the specified type
        and all of its elements are negative or zero; False, otherwise.

        :raises TypeError: If the elements of the numpy array are not negative
         and texcept is True.
    """
    # Validate it is a 2D numpy array.
    if not (flag := validate_type(array, dtype, texcept=texcept)):
        return flag

    # Validate the type of the elements.
    flag = flag and (np.all(array <= 0 if zero else array < 0))
    if not flag and texcept:
        # Format the option.
        zero_opt = " or zero" if zero else ""

        raise ValueError(
            f"Not all the elements of the numpy array are less than "
            f"zero{zero_opt}. Current values: {array}, less than "
            f"zero{zero_opt}: {tuple(array <= 0 if zero else array < 0)}."
        )

    return flag


def validate_type_positive(
    array: Any, dtype: Any, zero: bool = False, texcept: bool = True
) -> bool:
    """
        Function that validates that the array object is a numpy array of a
        the given type(s) and ALL its elements are positive. If the zero option
        is set to True, then the value can be zero.

        :param array: The array to validate.

        :param dtype: The type of the elements of the array.

        :param zero: A boolean flag that indicates if the value of the array
         elements can be zero.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the object is not a numpy array of the specified type and all
         its values are positive or zero. The latter depends on the value of the
         zero option. True, if an exception should be raised; False, otherwise.
         True, by default.

        :return: True, if the object is a numpy array of the specified type
        and all of its elements are positive or zero; False, otherwise.

        :raises TypeError: If the elements of the numpy array are not positive
         and texcept is True.
    """
    # Validate it is a 2D numpy array.
    if not (flag := validate_type(array, dtype, texcept=texcept)):
        return flag

    # Validate the type of the elements.
    flag = flag and (np.all(array >= 0 if zero else array > 0))
    if not flag and texcept:
        # Format the option.
        zero_opt = " or zero" if zero else ""

        raise ValueError(
            f"Not all the elements of the numpy array are greater than "
            f"zero{zero_opt}. Current values: {array}, greater than "
            f"zero{zero_opt}: {tuple(array >= 0 if zero else array > 0)}."
        )

    return flag


def validate_unique_columns(array: Any, texcept: bool = True) -> bool:
    """
        Function that validates that the array object is a numpy array of unique
        columns; i.e., there cannot be repeated columns.

        :param array: The array to validate.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the input is not a numpy array of unique column elements.
         True, if an exception should be raised; False otherwise. True, by
         default.

        :return: True, if the object is a numpy array of unique elements; False,
         otherwise.

        :raises TypeError: If the object is not a numpy array of unique elements
         and texcept is True.
    """
    # Validate it is a 2D numpy array.
    if not (flag := validate_ndarray(array, texcept=texcept)):
        return flag

    # Auxiliary variables.
    length = len(array[0])
    repeated = list()

    # Validate the column elements are unique.
    for i in range(length):
        for j in range(i + 1, length):
            if np.all(array[:, i] == array[:, j]):
                flag = False
                repeated.append((i, j))

    if not flag and texcept:
        # Raise the exception.
        raise ValueError(
            f"The array is not a numpy array of unique columns. Repeated "
            f"column index pairs: {tuple(repeated)}."
        )

    return flag


def validate_unique_entries(array: Any, texcept: bool = True) -> bool:
    """
        Function that validates that the array object is a numpy array of unique
        elements; i.e., if there is any element that appears more than once the
        numpy array is not an array of unique elements.

        :param array: The array to validate.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the input is not a numpy array of unique elements.
         True, if an exception should be raised; False otherwise. True, by
         default.

        :return: True, if the object is a numpy array of unique elements; False,
         otherwise.

        :raises TypeError: If the object is not a numpy array of unique elements
         and texcept is True.
    """
    # Validate it is a 2D numpy array.
    if not (flag := validate_ndarray(array, texcept=texcept)):
        return flag

    # Validate the element are unique.
    farray = array.flatten()
    flag = len(farray) == len(np.unique(farray))

    if not flag and texcept:
        # Repeated items.
        iset = dict(x for x in zip(*np.unique(farray, return_counts=True)))

        # Raise the exception.
        raise ValueError(
            f"The array is not a numpy array of unique elements. Repeated "
            f"elements and counts: {iset}."
        )

    return flag


def validate_unique_rows(array: Any, texcept: bool = True) -> bool:
    """
        Function that validates that the array object is a numpy array of unique
        rows; i.e., there cannot be repeated rows.

        :param array: The array to validate.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the input is not a numpy array of unique elements. True, if
         an exception should be raised; False otherwise. True, by default.

        :return: True, if the object is a numpy array of unique elements; False,
         otherwise.

        :raises TypeError: If the object is not a numpy array of unique elements
         and texcept is True.
    """
    # Validate it is a 2D numpy array.
    if not (flag := validate_ndarray(array, texcept=texcept)):
        return flag

    # Auxiliary variables.
    length = len(array)
    repeated = list()

    # Validate the elements are unique.
    for i in range(length):
        for j in range(i + 1, length):
            if np.all(array[i] == array[j]):
                flag = False
                repeated.append((i, j))

    if not flag and texcept:
        # Raise the exception.
        raise ValueError(
            f"The array is not a numpy array of unique rows. Repeated "
            f"row index pairs: {tuple(repeated)}."
        )

    return flag
