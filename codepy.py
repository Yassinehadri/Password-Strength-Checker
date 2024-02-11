import re
def check_password_strength(password):
    # Define criteria for password strength
    min_length = 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = bool(re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password))

    # Calculate strength score
    score = 0
    if len(password) >= min_length:
        score += 1
    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Evaluate strength level
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

# Example usage
password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password strength:", strength)


