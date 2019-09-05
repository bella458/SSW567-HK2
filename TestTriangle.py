# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: bella manoim
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
    
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
    
    def testIsocelesTriangle(self): 
        self.assertEqual(classifyTriangle(5,5,4),'Isoceles','5,5,4 is a Isoceles triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(0,0,1),'InvalidInput','0,0,1 is invalid')

    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 is invalid')

    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle('a','b',0),'InvalidInput','a,b,0 is invalid')
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

