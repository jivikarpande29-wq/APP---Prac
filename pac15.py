
import gc
import tracemalloc

# Create a Node class
class Node:
    def __init__(self):
        self.data = [0] * 100
        self.ref = self

# Create objects
def create_objects(n):
    for i in range(n):
        Node()

# Display memory usage
def show_memory(label):
    current, peak = tracemalloc.get_traced_memory()
    print(label, "->", round(current / 1024, 1), "KB")

# Start memory tracking
tracemalloc.start()

# Disable automatic garbage collection
gc.disable()

show_memory("Initial Memory")

# Create 5000 objects
create_objects(5000)
show_memory("After Creating Objects")

# Enable garbage collection debugging
gc.set_debug(gc.DEBUG_STATS)

# Manually collect garbage
collected = gc.collect()

# Disable debugging
gc.set_debug(0)

print("Objects Collected:", collected)

# Display memory after collection
show_memory("After Garbage Collection")

# Enable automatic garbage collection
gc.enable()

tracemalloc.stop()
