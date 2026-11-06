import numpy as np

# Create array
arr = np.arange(1, 11)
print("Original Array:", arr)

# Slicing
print("First five elements:", arr[:5])
print("Elements from index 3 to 7:", arr[3:8])
print("Alternate elements:", arr[::2])
print("Reverse array:", arr[::-1])

# Statistical operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting
print("After adding 5:", arr + 5)
print("After multiplying by 2:", arr * 2)