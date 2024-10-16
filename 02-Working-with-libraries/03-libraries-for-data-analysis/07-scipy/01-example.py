import numpy as np
from scipy import optimize, integrate, interpolate, linalg, stats
import matplotlib.pyplot as plt

# Optimization example: finding the minimum of a function
def func(x):
    return x**2 + 10*np.sin(x)

# Initial guess
x0 = 0

# Find the minimum
result = optimize.minimize(func, x0)
print("Optimization result:")
print(result)

# Integration example: integrating a function
def integrand(x):
    return np.exp(-x**2)

# Integrate from -inf to inf
integral, error = integrate.quad(integrand, -np.inf, np.inf)
print("\nIntegration result:")
print(f"Integral: {integral}, Error: {error}")

# Interpolation example: interpolating data points
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Create an interpolating function
interp_func = interpolate.interp1d(x, y, kind='cubic')

# Generate new x values for interpolation
x_new = np.linspace(0, 10, 100)
y_new = interp_func(x_new)

# Plot the original data points and the interpolated curve
plt.figure()
plt.plot(x, y, 'o', label='Original data')
plt.plot(x_new, y_new, '-', label='Interpolated curve')
plt.legend()
plt.title("Interpolation Example")
plt.show()

# Linear algebra example: solving a system of linear equations
A = np.array([[3, 2], [1, 4]])
b = np.array([1, 2])

# Solve for x in Ax = b
x_sol = linalg.solve(A, b)
print("\nLinear Algebra result:")
print(f"Solution x: {x_sol}")

# Statistics example: fitting a distribution to data
data = np.random.normal(loc=0, scale=1, size=1000)

# Fit a normal distribution to the data
mu, std = stats.norm.fit(data)
print("\nStatistics result:")
print(f"Fitted mean: {mu}, Fitted standard deviation: {std}")

# Plotting the histogram of the data and the fitted distribution
plt.figure()
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Data')

# Plot the PDF of the fitted distribution
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2, label='Fitted distribution')
plt.legend()
plt.title("Statistics Example")
plt.show()