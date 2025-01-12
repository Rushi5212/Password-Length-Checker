import re

def check_password_strength(password):
    # Criteria for strength checking
    length_criteria = len(password) >= 12
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    number_criteria = any(char.isdigit() for char in password)
    special_character_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    common_passwords = ['123456', 'password', '123456789', 'qwerty', 'abc123']

    # Check if the password is too common
    if password in common_passwords:
        return "Weak", "Your password is too common."

    # Calculate strength
    score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_character_criteria
    ])

    # Provide feedback
    if score == 5:
        return "Strong", "Your password is strong!"
    elif score >= 3:
        return "Moderate", "Consider adding more characters, numbers, or special symbols."
    else:
        return "Weak", "Your password is too weak. Use a mix of letters, numbers, and special symbols."

# Main function
if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    password = input("Enter a password to check its strength: ")

    strength, feedback = check_password_strength(password)
    print(f"Strength: {strength}")
    print(f"Feedback: {feedback}")
