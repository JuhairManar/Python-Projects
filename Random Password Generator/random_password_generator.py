import random
password="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*()-_=+[]{}|;:',.<>/?`"
pass_length=input(int("Enter the length of password"))

a="".join(random.sample(password,pass_length))

print("Your password is {a}")




import random
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
symbols = "!@#$%^&*()-_=+[]{}|;:',.<>/?`"

password_characters = random.choice(uppercase_letters) +random.choice(lowercase_letters) +random.choice(digits) + random.choice(symbols)

password_length = int(input("Enter the desired length of the password: "))

# Ensure the remaining characters in the password are randomly selected from all characters
remaining_characters = (
    uppercase_letters +
    lowercase_letters +
    digits +
    symbols
)

# Check if the desired password length is greater than 4 (already have one of each type)
if password_length > 4:
    password_characters += "".join(random.sample(remaining_characters, password_length - 4))
else:
    print("Password length should be at least 4 characters.")

# Shuffle the characters to make the password more random
password = "".join(random.sample(password_characters, password_length))

print(f"Your password is: {password}")
