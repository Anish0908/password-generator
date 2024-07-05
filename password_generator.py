import random
import string

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")

    character_set = lowercase_letters
    if use_uppercase:
        character_set += uppercase_letters
    if use_digits:
        character_set += digits
    if use_special:
        character_set += special_characters

    password = ''.join(random.choice(character_set) for _ in range(length))

    # Ensure the password contains at least one character from each selected set
    if use_uppercase and not any(char in uppercase_letters for char in password):
        password += random.choice(uppercase_letters)
    if use_digits and not any(char in digits for char in password):
        password += random.choice(digits)
    if use_special and not any(char in special_characters for char in password):
        password += random.choice(special_characters)

    # Shuffle the password to ensure randomness
    password = ''.join(random.sample(password, len(password)))

    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password (minimum 4 characters): "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_digits, use_special)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()

