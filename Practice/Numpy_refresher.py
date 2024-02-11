# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:42:30 2024

@author: Julie Waldroup

Basic and Advanced Python Methods

"""

import numpy as np

"""Basic Data Structures Refresher--------------------"""

#Arrays---

'''Array vs List

The key difference is that a list is dynamic ie can store
multiple data types and thus must store a lot more info
under the hood by comparison to an array'''

'''Copying Arrays

When slicing the subslice is not a copy, its a view and modifying it
will modify the original array'''

'''Concatenating

can use np.concatenate to join two+ arrays that are 1d+
    -can also specify the axis to join across
np.vstack and hstack concatenate vertically
    -dstack stacks along the third axis'''
    
x = np.array([1,2,3])
grid = np.array([[9,8,7],
                 [6,5,4]])

print('vstack: \n', np.vstack([x, grid]))
y = np.array([[10],[10]])
print('hstack: \n', np.hstack([grid, y]))

'''Splitting

splitting functions np.split, .hsplit, .vsplit work 
similarily'''

x = np.array([1,2,3,99,99,3,2,1])
x1,x2,x3 = np.split(x, [3,5]) #[3,5] specifies indices

grid = np.arange(16).reshape((4, 4))
print(grid)
upper, lower = np.vsplit(grid, [2])
print('vsplit: \n', upper)
print(lower)

#Lists---

#Dictionaries---

"Numpy--------------------------------------------------"

'''The reason numpy is so great is it's a flexible interface
to optimized computation with arrays of data.

Vectorization---

Vectorization through ufuncs

computation can be made fast using vectorized operations
    -these can be implemented through universal functions
    ie ufuncs
    
ufuncs avoid the slow time of looping that must first 
examine the object's type and find the correct function 
for each iteration

vectorized operation is a statically typed compiled routine
    -works by performing an operation on the entire array
    it pushes the loop into the compiled layer that underlies
    numpy and speeds up execution
    -eg computing 1.0/array to compute inverses is much faster
    than a for loop that takes 1.0/input[i] for each iteration
    
vectorized operations are implemented via ufuncs and basic ones
include
    -array arithmatic like add, powers, modulus
    -these are implemented through np.add, np.power, np.mod, etc
    -trig functions, logs, exp, etc
    
can create your own with frompyfunc() method

specialized ufuncs can be found in scipy.special and contains
many obscure mathematical functions 

Advanced ufunc features include specifying outputs eg
    -eg'''
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)
'''
    -can also do things like peform operation and output to every
    other element in output array
    -great for saving memory when performing computations on very
    large arrays
    
binary ufuncs (ones that act on two inputs) often have aggregates
that can be computed directly from the object
    -eg np.add.reduce() sums all the elements in the array
    -np.multiply.reduce() multiplies all elements in an array
    
Vectorization through Broadcasting

broadcasting is a simple set of rules for applying binary ufuncs
on arrays of different sizes

simple examples:
    -simplest example is adding a scalar to all elements of an array
    -a more complex example is adding a 1x3 array to a 3x3 array
    the 1d array is broadcasted and added to each row of the 3x3 array
    -even more complex a 1x3 added to a 3x1 = a 3x3 result

Rules of Broadcasting that determine the interaction between arrays:
    -1. if two arrays do not have the same # of dim, the shape of the one with
    fewer dimensions is padded with ones on its leading left side
    -2. if the shape of two arrays does not match in any dimension, then the
    array with shape equal to 1 in that dimension is stretched to match the other shape
    -3. if any dimension of the sizes disagree and neither is equal to 1, an error
    is raised
    
Broadcasting 1st example'''

'''Rule 2nd example'''

'''Rule 3rd example'''

'''
Aggregations---

Used in computing summary statistics of data

Number of common ones (numpy version is faster than python's built in)
    -np.sum,np.min,np.max
    -various statistical quantities such as means std etc
    


'''

