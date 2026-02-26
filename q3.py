def update_dictionary(dct, key, value):
    
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    
    if key in dct:
        print("Original value:", dct[key])
        
    dct[key] = value
    
    return dct


print(update_dictionary({}, "name", "Alice"))   # Output: {'name': 'Alice'}

print(update_dictionary({"age": 25}, "age", 26))    # Prints: Original value: 25    # Output: {'age': 26}
