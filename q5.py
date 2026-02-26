def check_divisibility(num, divisor):
    
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    
    # Validate numeric inputs
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise TypeError("Both num and divisor must be numeric")

    return num % divisor == 0


print(check_divisibility(10, 2))  # Expected: True

print(check_divisibility(7, 3))   # Expected: False
