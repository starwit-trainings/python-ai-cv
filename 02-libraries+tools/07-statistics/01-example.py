import statistics as stats

# Sample data
data = [2.3, 3.1, 4.7, 2.5, 3.9, 3.4, 2.8, 4.1, 3.6, 3.0]

# Mean
mean_value = stats.mean(data)
print(f"Mean: {mean_value}")

# Median
median_value = stats.median(data)
print(f"Median: {median_value}")

# Mode
# Adding a mode value to demonstrate mode function
data_with_mode = data + [3.1]
mode_value = stats.mode(data_with_mode)
print(f"Mode: {mode_value}")

# Standard Deviation
std_dev = stats.stdev(data)
print(f"Standard Deviation: {std_dev}")

# Variance
variance = stats.variance(data)
print(f"Variance: {variance}")

# Harmonic Mean
harmonic_mean_value = stats.harmonic_mean(data)
print(f"Harmonic Mean: {harmonic_mean_value}")

# Geometric Mean
geometric_mean_value = stats.geometric_mean(data)
print(f"Geometric Mean: {geometric_mean_value}")

# Additional functions
min_value = min(data)
max_value = max(data)
print(f"Min: {min_value}")
print(f"Max: {max_value}")

# Outputting the entire data set summary
summary = {
    'Mean': mean_value,
    'Median': median_value,
    'Mode': mode_value,
    'Standard Deviation': std_dev,
    'Variance': variance,
    'Harmonic Mean': harmonic_mean_value,
    'Geometric Mean': geometric_mean_value,
    'Min': min_value,
    'Max': max_value
}

print("\nSummary of Data:")
for key, value in summary.items():
    print(f"{key}: {value}")