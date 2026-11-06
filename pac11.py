import pandas as pd
import numpy as np

# Generate 10 random numbers
np.random.seed(42)
numbers = np.random.randint(1, 100, 10)

# Create Pandas Series
s = pd.Series(numbers)
print("Original Series:")
print(s)

# Indexing
print("Element at index 3:", s[3])
print("First five elements:")
print(s[:5])

# Filtering
print("Numbers greater than 50:")
print(s[s > 50])

# Statistical operations
print("Mean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())