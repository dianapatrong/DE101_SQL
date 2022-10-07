# Python Lab3: Numpy

## Create and activate the virtual environment 

```
pyenv virtualenv 3.9.0 lab3 
pyenv local lab3
```

## Install numpy 
```
pip install numpy==1.23.3 
```

# Exercises

## Exercise 1
Import numpy and print its version from a script

## Exercise 2 
Create a 1D array of numbers from 0 to 9 

## Exercise 3
From the 1D array of numbers from 0 to 9, extract odd numbers

## Exercise 4
From the 1D array of numbers from 0 to 9, replace all the odd numbers with `-1` 

## Exercise 5
From the 1D array of numbers from 0 to 9, replace all the odd numbers with `-1` without changing the original array

## Exercise 6
Get common items between `a` and `b` 

```python
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
```

## Exercise 7 
Get all items between 5 and 10 from `a`. 

```python 
a = np.arange(15)
```

## Exercise 8
Given two numpy arrays, calculate the element-wise addition.

```python
a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([[10,11,12],
              [13,14,15]])
```

## Exercise 9
Given a numpy array, multiply the array by a scalar `2`

``` python
a = np.array([[1,2,3],
              [4,5,6]])
```

## Exercise 10
Convert all the elements of a numpy array from float to integer 

```python
a = np.array([[2.5, 3.8, 1.5],
              [4.7, 2.9, 1.56]])
```

## Exercise 11
From 2 numpy arrays, extract the indexes in which the elements in the 2 arrays match

```python
a = np.array([1,2,3,4,5])
b = np.array([1,3,2,4,5])
```
