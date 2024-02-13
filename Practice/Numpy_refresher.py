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
    fewer dimensions shape is padded with ones on its leading left side
    -2. if the shape of two arrays does not match in any dimension, then the
    array with shape equal to 1 in that dimension is stretched to match the other shape
    -3. if any dimension of the sizes disagree and neither is equal to 1, an error
    is raised
    
Broadcasting 1st example'''

print('Broadcasting Ex')
M = np.ones((2,3))
a = np.arange(3)
print(M.shape, a.shape)
print(M, a)
#a has fewer dimensions so its padded on the left with ones to be
#(3,) -> (1,3)
#Then a is stretched so the first dimensions agree
#(1,3) -> (2,3)
print(np.add(M,a))

'''Broadcasting 2nd example'''

print(a)
a = np.arange(3).reshape((3,1))
print(a)
b = np.arange(3)
#rule one says pad b to shape (1,3)
#rule 2 says stretch a and b to (3,3)
print(np.add(a,b))

'''
When is broadcasting useful?

when centering an array or plotting 2d functions are two examples

Aggregations---

Used in computing summary statistics of data

Number of common ones (numpy version is faster than python's built in)
    -np.sum,np.min,np.max
    -various statistical quantities such as means std etc

Fancy Indexing---

like simple indexing but passes arrays of indices in place of scalars
good for accessing and modifying complex subsets of an array's values

its conceptually simple using an array of indices to access multiple e
lements at once

eg
'''
print('Fancy indexing example')
x = np.random.randint(100, size=10)
ind = [3,7,4]
print(x)
print(x[ind])

'''The shape of the result reflects the shape of the index arrays
rather than the shape of the array being indexed

ie we can index x with a 2x2 array and get a 2x2 result

Can combine simple and fancy indices as well as slicing & masking

Useful for
    -partitioning datasets
    -computing histograms by hand
    
Sorting Arrays---

algorithms for sorting values in numpy arrays
there are several but we can fast sort using

np.sort and np.argsort

np.sort uses a quicksort algorithm which can be used along different
axes

np.argsort returns indices of position of smallest to largest element

partial sorting can be done with np.partition
    -finds the k smallest values in the array 
    -returns array with k values to the left of the partition
    and the rest to the right in arbitrary order
    
Structured Arrays---

provide efficient storage for compound hetergeneous data
    -usually pandas dataframes are better
    
spse several categories of data like name, weight, age

can create a structured array using a compound data type 
specification
ie
'''
print('Structured Array Example')
#first create container array
data = np.zeros(4, dtype={'names':('name','age','weight'),
                          'formats':('U10','i4','f8')})
print(data.dtype)
print(data)
'''
U10 is unicode string of max length 10
i4 is 4byte integer (32 bit)
f8 is 8byte (64 bit) float

we can now fill the container array with lists of values
'''

data['name'] = ['Alice','Bob','Cathy','Doug']
data['age'] = [25,45,37,19]
data['weight'] = [55.0,85.5,68,61.5]
print(data)

'''
Can now access the values either by index or by name
eg
'''
#get names where age is under thirty
print(data[data['age'] < 30]['name'])

'''
Creating Structured Arrays
    -can be done as before (the dictionary method)
    -dictionary method but with np dtypes instead of U10 codes
    -or as a list of tuples
    
Can even create structured arrays with lists of different dimensions
'''
#tuple creation example
tp = np.dtype([('id','i8'),('mat','f8', (3,3))])
x = np.zeros(1, dtype=tp)
print(x)
print(x[0])
print('--')
print(x['mat'][0])
print(x['id'])

'''
RecordArrays---

np.recarray class which is identical to structured arrays except with
a new feature 
    -fields can be accessed as attributes rather than as dictionary keys

so instead of 
'''
print('Record arrays')
print(data['age'])
data_rec = data.view(np.recarray)
print(data_rec.age)
