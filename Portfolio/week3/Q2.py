# Write a program that simulates the way in which a user might choose a password. The program should prompt for a new password, and then prompt again. If the two passwords entered are the same the program should say "Password Set" or similar, otherwise it should report an error
def set_password():
    # Prompt the user to enter a new password
    password1 = input("Enter a new password: ")
    
    # Prompt the user to re-enter the password for confirmation
    password2 = input("Re-enter the password: ")
    
    # Check if the two passwords match
    if password1 == password2:
        print("Password Set")
    else:
        print("Error: Passwords do not match. Please try again.")

# Run the program
set_password()