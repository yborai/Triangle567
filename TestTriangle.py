# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangles(self): 
        self.assertEqual(classifyTriangle(2,1,2),'Isosceles','2,1,2 should be isosceles')
        self.assertNotEqual(classifyTriangle(2,2,2),'Isosceles','2,2,2 should be equilateral')


    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be scalene')

    def testValidTriangles(self):
        self.assertEqual(classifyTriangle(201,3,4),'InvalidInput','201,3,4 should be InvalidInput')
        self.assertEqual(classifyTriangle(2,201,4),'InvalidInput','2,201,4 should be InvalidInput')
        self.assertEqual(classifyTriangle(1,3,201),'InvalidInput','1,3,201 should be InvalidInput')
        self.assertEqual(classifyTriangle(-1,3,4),'InvalidInput','-1,3,4 should be InvalidInput')
        self.assertEqual(classifyTriangle(2,-1,4),'InvalidInput','2,-1,4 should be InvalidInput')
        self.assertEqual(classifyTriangle(1,3,-1),'InvalidInput','1,3,-1 should be InvalidInput')
        self.assertEqual(classifyTriangle(1,1,2),'NotATriangle','1,1,2 should be NotATriangle')





if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
