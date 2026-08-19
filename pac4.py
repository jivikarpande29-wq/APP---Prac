


def fibonacci_iterative(n):

    # If n is 0
    if n == 0:
        return 0

    # If n is 1
    elif n == 1:
        return 1

    
    a, b = 0, 1

    
    for _ in range(2, n + 1):

        # Add previous two numbers
        c = a + b

        # Move b to a
        a = b

        # Move c to b
        b = c

    
    return b



n = int(input("Enter the value of n: "))
result = fibonacci_iterative(n)

print("Fibonacci number is:", result)