# JD - Password Strength Checker Assignment

# 1. Get user input and save it to a variable
password = input("What is your password: ")

# 2. Check each individual rule
has_length = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)

# Define a set of common symbols to check against
symbols = "!@#$%^&*"
has_symbol = any(char in symbols for char in password)

# 3. Print True/False results for each rule
print(f"\nAt least 8 characters: {has_length}")
print(f"Has an uppercase letter: {has_upper}")
print(f"Has a lowercase letter: {has_lower}")
print(f"Has a number: {has_digit}")
print(f"Has a symbol: {has_symbol}")

# 4. Calculate total score (how many rules are met)
rules_met = sum([has_length, has_upper, has_lower, has_digit, has_symbol])

# Determine strength rating
if rules_met == 5:
    strength = "Strong"
elif rules_met >= 3:
    strength = "Medium"
else:
    strength = "Weak"

print(f"\nYour password strength is: {strength}")

# 5. Provide feedback on missing rules if the password is not Strong
if strength != "Strong":
    missing_items = []
    
    if not has_length:
        missing_items.append("at least 8 characters")
    if not has_upper:
        missing_items.append("an uppercase letter")
    if not has_lower:
        missing_items.append("a lowercase letter")
    if not has_digit:
        missing_items.append("a number")
    if not has_symbol:
        missing_items.append("a symbol")
        
    # Join missing elements with a comma
    print(f"To make it Strong, add: {', '.join(missing_items)}")
