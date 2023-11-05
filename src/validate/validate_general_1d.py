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

# User defined.
import src.validate.validate_general as vgeneral

# ##############################################################################
# Global Variables
# ##############################################################################


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'validate' Functions
# ------------------------------------------------------------------------------


def validate_ndarray(array: Any, texcept: bool = True) -> bool:
    """
        Function that validates that the array object is a one dimensional numpy
        array.

        :param array: The object to validate.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the object is not a oned dimensional numpy array. True, if an
         exception should be raised; False, otherwise. True, by default.

        :return: True, if the input is a one dimensional numpy array; False,
         otherwise.

        :raises TypeError: If the object is not a one dimensional numpy array
         and texcept is True.
    """
    # Check that the object a numpy array.
    flag = isinstance(array, np.ndarray)
    if not flag and texcept:
        raise TypeError(
            f"The array is not a numpy array. Current type: {type(array)}"
        )

    # Check that the object is a 1D numpy array.
    flag = flag and array.ndim == 1
    if not flag and texcept:
        raise ValueError(
            f"The array is not a one dimensional array. Current shape: "
            f"{array.shape}."
        )

    return flag


def validate_shape(array: Any, shape: int, texcept: bool = True) -> bool:
    """
        Function that validates that the array object is a numpy array of the
        specified shape.

        :param array: The array to validate.

        :param shape: The integer that specifies the shape of the array.

        :param texcept: If an exception must be thrown if the array is not of
         the specified shape. True, if an exception should be raised; False,
         otherwise. True, by default.

        :return: True, if the array is of the specified shape; False, otherwise.
    """
    # Checks the length of the array is a positive integer, can include zero.
    vgeneral.validate_type_positive(shape, int, zero=True)

    # Validate it is a 1D numpy array.
    if not (flag := validate_ndarray(array, texcept=texcept)):
        return flag

    # Validate the length of the array.
    flag = array.shape[0] == shape
    if not flag and texcept:
        raise ValueError(
            f"The array is not a one dimensional array of the specified "
            f"length. Current length: {array.shape}."
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
    # Validate it is a 1D numpy array.
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
        the given type(s) and ALL its elements are negative. If the zero option
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
    # Validate it is a 1D numpy array.
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
    # Validate it is a 1D numpy array.
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


def validate_unique(array: Any, texcept: bool = True) -> bool:
    """
        Function that validates that the array object is a numpy array of unique
        elements.

        :param array: The array to validate.

        :param texcept: A boolean flag that indicates if an exception should be
         raised if the input is not a numpy array of unique elements. True, if
         an exception should be raised; False otherwise. True, by default.

        :return: True, if the object is a numpy array of unique elements; False,
         otherwise.

        :raises TypeError: If the object is not a numpy array of unique elements
         and texcept is True.
    """
    # Validate it is a 1D numpy array.
    if not (flag := validate_ndarray(array, texcept=texcept)):
        return flag

    # Validate the elements are unique.
    flag = len(np.unique(array)) == len(array)
    if not flag and texcept:
        # Get the number of times each element is repeated.
        repeated = dict((x, y) for x, y in np.unique(array, return_counts=True))

        # Raise the exception.
        raise TypeError(
            f"The array is not a numpy array of unique elements. Values and "
            f"count: {repeated}."
        )

    return flag
