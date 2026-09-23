#NS, password strenght checker

password = input("whats your password? ")
lenghth = False
upper = False
lower = False
symbol = False
strenghth = 0
number = False 

for letter in password:
    if letter.isupper():
        upper = True

    if letter.islower():
        lower = True

    if letter.isnumeric():
        number = True

    if letter in "!@#$%^&*()" :
        symbol = True

print(f"At least 8 characters: {lenghth}")
print(f"Has an uppercase letter: {upper}")
print(f"Has a lowercase letter: {lower}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")

rules = ([lenghth, upper, lower, symbol, number])
sum = strenghth

if rules <= 2
strenghth = weak