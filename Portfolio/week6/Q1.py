# Write a function that accepts a positive integer as a parameter and then returns a representation of that number in binary (base 2). Hint: This is in many ways a trick question. Think!
def decimal_to_binary(decimal_number):
    if decimal_number <= 0:
        return "Input must be a positive integer"
    
    binary_representation = bin(decimal_number)[2:]  # Using [2:] to remove the '0b' prefix
    return binary_representation

# Example usage:
positive_integer = 10
binary_result = decimal_to_binary(positive_integer)
print(f"The binary representation of {positive_integer} is: {binary_result}")