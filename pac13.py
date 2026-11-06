
import threading
import time

# Task 1: Count numbers
def count_numbers():
    for i in range(1, 6):
        print("Count:", i)
        time.sleep(1)

# Task 2: Calculate squares
def calculate_squares():
    for i in range(1, 6):
        print("Square of", i, "=", i * i)
        time.sleep(1)

# Task 3: Calculate cubes
def calculate_cubes():
    for i in range(1, 6):
        print("Cube of", i, "=", i ** 3)
        time.sleep(1)

# Main function
def main():
    t1 = threading.Thread(target=count_numbers)
    t2 = threading.Thread(target=calculate_squares)
    t3 = threading.Thread(target=calculate_cubes)

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for all threads to finish
    t1.join()
    t2.join()
    t3.join()

    print("All tasks completed.")

# Run program
if __name__ == "__main__":
    main()
