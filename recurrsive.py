def factorial(n):
    """
    Calculates the factorial of a positive integer n recursively.
    """
    # 1. The Base Case: This tells the function when to stop.
    if n == 0 or n == 1:
        return 1
        
    # 2. The Recursive Case: The function calls itself with a smaller number.
    else:
        return n * factorial(n - 1)

# --- Example Usage ---
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}") 
# Output: The factorial of 5 is 120
