# Computers are commonly used in encryption. A very simple form of encryption (more accurately "obfuscation") would be to remove the spaces from a message and reverse the resulting string. Write, and test, a function that takes a string containing a message and "encrypts" it in this way.

def encrypt_message(message):
    # Remove spaces from the message
    message_without_spaces = message.replace(" ", "")
    
    # Reverse the resulting string
    encrypted_message = message_without_spaces[::-1]
    
    return encrypted_message

# Example usage:
original_message = "This is a simple message."
encrypted_message = encrypt_message(original_message)

print("Original Message: ", original_message)
print("Encrypted Message: ", encrypted_message)