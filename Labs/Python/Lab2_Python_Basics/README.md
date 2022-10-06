# Python Lab2: Basics 

## Set
* Sets are unordered.
* Set elements are unique. Duplicate elements are not allowed.
* A set itself may be modified, but the elements contained in the set must be of an immutable type.

You can define a set with the built-in `set()` function:

```python
>>> my_set = set(["DE101", "SQL", "Python", "Python"])
>>> my_set
{'SQL', 'DE101', 'Python'}
```

## List 

* Created by placing elements inside square brackets [], separated by commas.
* Can have any number of items and they may be of different types (integer, float, string, etc.).
* Can also have another list as an item. This is called a nested list.


```python
# empty list
my_list = []

# list with mixed data types
my_list = [1, "Hello", 3.4]

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]
```

## Dictionary

A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.
You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). 
A colon (:) separates each key from its associated value:

```python
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
```

## Tuple

A tuple in Python is similar to a list. The difference between the two is that we cannot change the  elements of a tuple 
once it is assigned whereas we can change the elements of a list.

A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them.

A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).

```python
# Empty tuple
my_tuple = ()

# Tuple having integers
my_tuple = (1, 2, 3)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
```

# Exercises
All exercises must be solved using plain python (no libraries at this moment).

## Exercise 1
Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

```
Input: 20,30
Output: 600

Input: 40,30
Output: 70 
```

## Exercise 2
Given a student with their marks, create a dictionary and find the average of score of each student. 

* Peter: 25,36,47,45
* Wong: 85,74,69,47
* Nick: 65,35,87,14
* Michelle: 74,12,36,75

```
Output: [38, 68, 50, 49]
```

## Exercise 3
Given a non-empty string, write a python function to check if the string is palindrome or not. 
A string is said to be palindrome if the reverse of the string is the same as string. 

```
Input : 'radar'
Output : True

Input : 'radix'
Output : False
```


## Exercise 4
Write a python function to check if a number is even or odd

## Exercise 5
Given a dictionary in Python, write a Python program to find the sum of all items in the dictionary.

```
Input : {'a': 100, 'b':200, 'c':300}
Output : 600

Input : {'x': 25, 'y':18, 'z':45}
Output : 88
```

## Exercise 6
Write a program to iterate a given list and count the occurrence of each element,  create a dictionary to show the count of each element.

```
Input: [11, 45, 8, 11, 23, 45, 23, 45, 89]
Output: {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
```

## Exercise 7
Iterate a given list and check if a given element exists as a key's value in a dictionary. If not, delete it from the list.

```
Input: [47, 64, 69, 37, 76, 83, 95, 97], {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
Output: [47, 69, 76, 97]
```

