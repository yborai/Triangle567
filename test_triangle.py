# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """define multiple sets of tests as functions with names that begin"""

    def test_right_triangle_a(self):
        """Tests one variation of a right triangle"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        """Tests another variation of a right triangle"""
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def test_equilateral_triangles(self):
        """test for an equilateral triangle"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_isosceles_triangles(self):
        """test for an isosceles triangle"""
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene', '2,3,4 should be scalene')

    def test_valid_triangles(self):
        """Tests for valid triangles"""
        self.assertEqual(
            classify_triangle(201, 3, 4),
            'InvalidInput',
            '201,3,4 should be InvalidInput'
        )
        self.assertEqual(
            classify_triangle(2, 201, 4),
            'InvalidInput',
            '2,201,4 should be InvalidInput'
        )
        self.assertEqual(
            classify_triangle(1, 3, 201),
            'InvalidInput',
            '1,3,201 should be InvalidInput'
        )
        self.assertEqual(
            classify_triangle(-1, 3, 4),
            'InvalidInput',
            '-1,3,4 should be InvalidInput'
        )
        self.assertEqual(
            classify_triangle(2, -1, 4),
            'InvalidInput',
            '2,-1,4 should be InvalidInput'
        )
        self.assertEqual(
            classify_triangle(1, 3, -1),
            'InvalidInput',
            '1,3,-1 should be InvalidInput'
        )
        self.assertEqual(
            classify_triangle(1, 1, 2),
            'NotATriangle',
            '1,1,2 should be NotATriangle'
        )

if __name__ == '__main__':
    print 'Running unit tests'
    unittest.main()
