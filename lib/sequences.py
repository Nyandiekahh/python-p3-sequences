#!/usr/bin/env python3

def print_fibonacci(length):
    # If the desired length is less than or equal to 0, print and return an empty list
    if length <= 0:
        print([])
        return []

    # Initialize the first two numbers of the Fibonacci sequence
    fibonacci_sequence = [0, 1]

    # If the desired length is 1, print and return the first number
    if length == 1:
        print([0])
        return [0]

    # Generate the Fibonacci sequence up to the desired length
    while len(fibonacci_sequence) < length:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    
    # Print the generated Fibonacci sequence
    print(fibonacci_sequence)
    return fibonacci_sequence

# Example usage
if __name__ == "__main__":
    length = 9
    print_fibonacci(length)
