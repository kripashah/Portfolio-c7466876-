# Another way to hide a message is to include the letters that make it up within seemingly random text. The letters of the message might be every fifth character, for example. Write and test a function that does such encryption. It should randomly generate an interval (between 2 and 20), space the message out accordingly, and should fill the gaps with random letters. The function should return the encrypted message and the interval used.
# For example, if the message is "send cheese", the random interval is 2, and for clarity the random letters are not random: send cheese s e n d c h e e s e sxyexynxydxy cxyhxyexyexysxye
import random

def encrypt_message(message):
    interval = random.randint(2, 20)
    random_letters = "abcdefghijklmnopqrstuvwxyz"

    encrypted_message = ""
    for i, char in enumerate(message):
        if char.isalpha():
            encrypted_message += char
        else:
            encrypted_message += random.choice(random_letters)

        if i % interval == interval - 1:
            encrypted_message += ' '

    return encrypted_message, interval

def decrypt_message(encrypted_message, interval):
    decrypted_message = ""
    words = encrypted_message.split()
    for word in words:
        decrypted_message += ''.join(c for i, c in enumerate(word) if i % interval == interval - 1)
    return decrypted_message

# Example usage:
message = "send cheese"
encrypted_message, interval_used = encrypt_message(message)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Interval Used: {interval_used}")

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, interval_used)
print(f"Decrypted Message: {decrypted_message}")