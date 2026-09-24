#NS, password strenght checker

password = input("What's your password? ")


length= len(password) >= 8
upper = False
lower = False
number = False
symbol = False
strength = 0

for letter in password:
    if letter.isupper():
        upper = True
    elif letter.islower():
        lower = True
    elif letter.isnumeric():
        number = True
    elif letter in "!@#$%^&*()":
        symbol = True


print(f"At least 8 characters: {length}")
print(f"Has an uppercase letter: {upper}")
print(f"Has a lowercase letter: {lower}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")


score = sum([length, upper, lower, symbol, number])


if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print(f"Your password strength is: {strength}")


if strength != "Strong":
    missing_items = []
    
    if not length:
        missing_items.append("at least 8 characters")
    if not upper:
        missing_items.append("an uppercase letter")
    if not lower:
        missing_items.append("a lowercase letter")
    if not number:
        missing_items.append("a number")
    if not symbol:
        missing_items.append("a symbol")
        
    print(f"To make it Strong, add: {', '.join(missing_items)}")