"""
    File that contains the unit test for the functions in the file
    validate_general_2d.py.
"""
import random

# ##############################################################################
# Imports
# ##############################################################################


# General
import numpy as np
import unittest

from typing import Union

# User defined
import src.validate.validate_general_2d as vgeneral


# ##############################################################################
# Classes
# ##############################################################################


class TestValidateGeneral2D(unittest.TestCase):
    """
        Class that contains the tests for the validation of 2D lattices.
    """

    def test_validate_ndarray(self):
        """
            Test the function validate_ndarray.
        """
        # Broad selection of types to test.
        types = (list, tuple, dict, int, float, str, bool, complex)

        # ----------------------------------------------------------------------
        # Test 1: The input is a two-dimensional numpy array.
        # ----------------------------------------------------------------------

        array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertTrue(vgeneral.validate_ndarray(array))

        # ----------------------------------------------------------------------
        # Test 2 and Test 3.
        # ----------------------------------------------------------------------

        # Test each type.
        for dtype in types:
            # Set the type of the object accordingly.
            array = dtype(([1, 3],)) if dtype in types[:3] else dtype(1)

            # ------------------------------------------------------------------
            # Test 2: The input is not a numpy array.
            # ------------------------------------------------------------------

            self.assertFalse(vgeneral.validate_ndarray(array, texcept=False))

            # ------------------------------------------------------------------
            # Test 3: The input is not a numpy array and an exception should be
            # raised.
            # ------------------------------------------------------------------

            with self.assertRaises(TypeError):
                vgeneral.validate_ndarray(array, texcept=True)

        # ----------------------------------------------------------------------
        # Test 4: The input is a numpy array with only 1 dimension.
        # ----------------------------------------------------------------------

        # A multidimensional array.
        array = np.array([1, 2, 3, 4, 5, 6])

        # Test for one dimension.
        self.assertFalse(vgeneral.validate_ndarray(array, texcept=False))

        with self.assertRaises(ValueError):
            vgeneral.validate_ndarray(array, texcept=True)

    def test_validate_shape(self):
        """
            Test the function validate_shape.
        """
        # Auxiliary variables.
        values = [[3 * x + y + 1 for y in range(3)] for x in range(3)]
        array = np.array(values, dtype=int)

        # ----------------------------------------------------------------------
        # Test 1: The input is a numpy array with the specified shape.
        # ----------------------------------------------------------------------

        # Correct shape.
        self.assertTrue(vgeneral.validate_shape(array, (3, 3)))

        # Wrong length.
        self.assertFalse(vgeneral.validate_shape(array, (3, 2), texcept=False))
        #
        # An exception should be raised.
        with self.assertRaises(ValueError):
            vgeneral.validate_shape(array, (3, 2))

        # ----------------------------------------------------------------------
        # Test 2: The shape is not a 2-tuple of integers.
        # ----------------------------------------------------------------------

        # Change the shape of the array.
        ts: Union[int, tuple] = 3
        array = np.array(values, dtype=int)

        # Test for a non-integer shape.
        with self.assertRaises(TypeError):
            self.assertFalse(vgeneral.validate_shape(array, ts, texcept=False))

        # Test for a shape with a negative integer in the first entry.
        ts = (-3, 3)
        with self.assertRaises(TypeError):
            self.assertFalse(vgeneral.validate_shape(array, ts, texcept=False))

        # Test for a shape with a negative integer in the second entry.
        ts = (3, -3)
        with self.assertRaises(TypeError):
            self.assertFalse(vgeneral.validate_shape(array, ts, texcept=False))

        # Test for a shape with a zero integer in the first entry.
        ts = (0, 3)
        with self.assertRaises(TypeError):
            self.assertFalse(vgeneral.validate_shape(array, ts, texcept=False))

        # Test for a shape with a zero integer in the second entry.
        ts = (3, 0)
        with self.assertRaises(TypeError):
            self.assertFalse(vgeneral.validate_shape(array, ts, texcept=False))

    def test_validate_type(self):
        """
            Test the function validate_type.
        """
        # Auxiliary variables.
        ntypes = (int, float, complex)
        values = [[3 * x + y for y in range(2)] for x in range(3)]

        for dtype in ntypes:
            # ------------------------------------------------------------------
            # Test 1: The input is a numpy array of the specified type.
            # ------------------------------------------------------------------

            array = np.array(values, dtype=dtype)
            self.assertTrue(vgeneral.validate_type(array, dtype))

            # ------------------------------------------------------------------
            # Test 2: The input is a numpy array of a different type.
            # ------------------------------------------------------------------

            # Change the type of the array.
            tdtype = [x for x in ntypes if x != dtype][0]
            array = np.array(values, dtype=tdtype)

            # Test for different types.
            self.assertFalse(
                vgeneral.validate_type(array, dtype, texcept=False)
            )

            # An exception should be raised.
            with self.assertRaises(TypeError):
                vgeneral.validate_type(array, dtype, texcept=True)

    def test_validate_type_negative(self):
        """
            Test the function validate_type_negative.
        """
        # Auxiliary variables.
        dtypes = (float, int)
        values = [
            ([0] + [-random.randint(1, 10) for _ in range(3)]) for _ in range(3)
        ]

        for dtype in dtypes:
            # Set the type of the object accordingly.
            array = np.array(values, dtype=dtype)

            # ------------------------------------------------------------------
            # Test 1: The input is a numpy array of negative elements.
            # ------------------------------------------------------------------

            self.assertTrue(
                vgeneral.validate_type_negative(array, dtype, zero=True)
            )

            # An exception should be raised.
            with self.assertRaises(ValueError):
                vgeneral.validate_type_negative(array, dtype, texcept=True)

            # ------------------------------------------------------------------
            # Test 2: The input is a numpy array of positive elements.
            # ------------------------------------------------------------------

            # Change the sign of the elements.
            array = -np.array(values, dtype=dtype)

            # Test for negative elements.
            self.assertFalse(
                vgeneral.validate_type_negative(array, dtype, texcept=False)
            )

            # An exception should be raised.
            with self.assertRaises(ValueError):
                vgeneral.validate_type_negative(array, dtype, texcept=True)

    def test_validate_type_positive(self):
        """
            Test the function validate_type_positive.
        """
        # Auxiliary variables.
        dtypes = (float, int)
        values = list(
            ([0] + [random.randint(1, 10) for _ in range(2)]) for _ in range(3)
        )

        for dtype in dtypes:
            # Set the type of the object accordingly.
            array = np.array(values, dtype=dtype)

            # ------------------------------------------------------------------
            # Test 1: The input is a numpy array of positive elements.
            # ------------------------------------------------------------------

            self.assertTrue(
                vgeneral.validate_type_positive(array, dtype, zero=True)
            )

            # An exception should be raised.
            with self.assertRaises(ValueError):
                vgeneral.validate_type_positive(array, dtype, texcept=True)

            # ------------------------------------------------------------------
            # Test 2: The input is a numpy array of negative elements.
            # ------------------------------------------------------------------

            # Change the sign of the elements.
            array = np.array(values, dtype=dtype)

            # Test for negative elements.
            self.assertFalse(
                vgeneral.validate_type_positive(array, dtype, texcept=False)
            )

            # An exception should be raised.
            with self.assertRaises(ValueError):
                vgeneral.validate_type_positive(array, dtype, texcept=True)

    def test_validate_unique_columns(self):
        """
            Test the function validate_unique_columns.
        """
        # Auxiliary variables.
        values = [[1, 1, 3], [1, 1, 3], [4, 5, 6]]
        array = np.array(values, dtype=int)

        # ----------------------------------------------------------------------
        # Test 1: The input is a numpy with unique elements.
        # ----------------------------------------------------------------------

        self.assertTrue(vgeneral.validate_unique_columns(array))

        # ----------------------------------------------------------------------
        # Test 2: The input is a numpy array with repeated rows.
        # ----------------------------------------------------------------------

        # Duplicate the values.
        values += values
        array = np.array(values, dtype=int)

        # Test for duplicates.
        self.assertFalse(vgeneral.validate_unique_rows(array, texcept=False))

        # An exception should be raised.
        with self.assertRaises(ValueError):
            vgeneral.validate_unique_rows(array, texcept=True)

    def test_validate_unique_entries(self):
        """
            Test the function validate_unique_entries.
        """
        # Auxiliary variables.
        values = [[3 * x + y for y in range(3)] for x in range(3)]
        array = np.array(values, dtype=int)

        # ----------------------------------------------------------------------
        # Test 1: The input is a numpy with unique elements.
        # ----------------------------------------------------------------------

        self.assertTrue(vgeneral.validate_unique_entries(array))

        # ----------------------------------------------------------------------
        # Test 2: The input is a numpy array with repeated elements.
        # ----------------------------------------------------------------------

        # Duplicate the values.
        values += values
        array = np.array(values, dtype=int)
        #
        # Test for duplicates.
        self.assertFalse(vgeneral.validate_unique_entries(array, texcept=False))
        #
        # An exception should be raised.
        with self.assertRaises(ValueError):
            vgeneral.validate_unique_entries(array, texcept=True)

    def test_validate_unique_rows(self):
        """
            Test the function validate_unique_rows.
        """
        # Auxiliary variables.
        values = [[1, 2, 3], [4, 5, 6]]
        array = np.array(values, dtype=int)

        # ----------------------------------------------------------------------
        # Test 1: The input is a numpy with unique elements.
        # ----------------------------------------------------------------------

        self.assertTrue(vgeneral.validate_unique_rows(array))

        # ----------------------------------------------------------------------
        # Test 2: The input is a numpy array with repeated rows.
        # ----------------------------------------------------------------------

        # Duplicate the values.
        values += values
        array = np.array(values, dtype=int)

        # Test for duplicates.
        self.assertFalse(vgeneral.validate_unique_rows(array, texcept=False))

        # An exception should be raised.
        with self.assertRaises(ValueError):
            vgeneral.validate_unique_rows(array, texcept=True)
