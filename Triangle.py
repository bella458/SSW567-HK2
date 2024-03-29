# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@author: Bella Manoim
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    # @bm fixed that b should be <=0 not b<=b
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) or isinstance(b,int) or isinstance(c,int)):
        return 'InvalidInput';
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    # @bm fixed the logic here to add instead of subtract the two sides that the third should be greater than
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    # @bm fixed that we need to check a = b = c for an equilateral
    if a == b and b == c:
        return 'Equilateral'
    # @bm we were multiplying by 2 instead of squaring. fixed to square the sides and check for all sides
    elif ((a * a) + (b * b)) == (c * c):
        return 'Right'
    elif ((a * a) + (c * c)) == (b * b):
        return 'Right'
    elif ((c * c) + (b * b)) == (a * a):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    # @bm added logic for isoceles
    elif ((a == b and a != c) or (b == c and b != a) or (a == c and a != b)):
        return 'Isoceles'
