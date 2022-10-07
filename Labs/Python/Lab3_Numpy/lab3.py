import numpy as np

print(f"Numpy version: {np.__version__}")

# Exercise 2
arr = np.arange(10)
print(f"Exercise 2 solution: {arr}")

# Exercise 3
arr2 = arr[arr % 2 == 1]
print(f"Exercise 3 solution: {arr2}")

# Exercise 4
arr[arr % 2 == 1] = -1
print(f"Exercise 4 solution: {arr}")

# Exercise 5
arr = np.arange(10)
arr5 = np.where(arr % 2 == 1, -1, arr)
print(f"Exercise 5 solution: {arr5}")

# Exercise 6
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
c = np.intersect1d(a, b)
print(f"Exercise 6 solution: {c}")

# Exercise 7
a = np.arange(15)

# Method 1
a1 = np.where((a >= 5) & (a <= 10))
print(f"Exercise 7 solution: {a[a1]}")

# Method 2
a2 = np.where(np.logical_and(a >= 5, a <= 10))
print(f"Exercise 7 solution: {a[a2]}")

# Method 3
a3 = a[(a >= 5) & (a <= 10)]
print(f"Exercise 7 solution: {a[a3]}")

# Exercise 8
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[10, 11, 12],
              [13, 14, 15]])

c = a + b
print(f"Exercise 8 solution: \n{c}")

# Exercise 9
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = 2*a
print(f"Exercise 9 solution: \n{b}")

# Exercise 10
a = np.array([[2.5, 3.8, 1.5],
              [4.7, 2.9, 1.56]])
b = a.astype('int')
print(f"Exercise 10 solution: \n{b}")

# Exercise 11
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 3, 2, 4, 5])
print(f"Exercise 11 solution: {(np.where(a == b))}")

