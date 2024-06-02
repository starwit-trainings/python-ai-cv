import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

print("Array a:", a)
print("Array b:", b)

# Array operations
sum_ab = a + b
diff_ab = a - b
prod_ab = a * b
quot_ab = a / b

print("\nSum of a and b:", sum_ab)
print("Difference of a and b:", diff_ab)
print("Product of a and b:", prod_ab)
print("Quotient of a and b:", quot_ab)

# Universal functions (ufuncs)
sqrt_a = np.sqrt(a)
exp_a = np.exp(a)

print("\nSquare root of a:", sqrt_a)
print("Exponential of a:", exp_a)

# Aggregate functions
sum_a = np.sum(a)
mean_a = np.mean(a)
std_a = np.std(a)

print("\nSum of elements in a:", sum_a)
print("Mean of elements in a:", mean_a)
print("Standard deviation of elements in a:", std_a)

# Reshaping arrays
c = np.arange(1, 13).reshape(3, 4)
print("\nArray c reshaped to 3x4:\n", c)

# Indexing and slicing
print("\nElement at (2, 3) in c:", c[2, 3])
print("First row of c:", c[0, :])
print("First column of c:", c[:, 0])

# Boolean indexing
even_elements = c[c % 2 == 0]
print("\nEven elements in c:", even_elements)

# Broadcasting
d = np.array([1, 2, 3])
e = np.array([[4], [5], [6]])
broadcast_result = d + e
print("\nBroadcasting result of d + e:\n", broadcast_result)