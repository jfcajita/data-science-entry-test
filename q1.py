def swap(x, y):
    
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    
    # Check if both are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swap using arithmetic (no temp variable)
    x = x + y
    y = x - y
    x = x - y

    return x, y


print(swap("Apple", 10))   # Not numeric → returns -1

print(swap(9, 17))         # Numeric → prints swapped values (17, 9)
