# NS, number information

for number in range(1,21):
    if number % 2 == 0 and number % 5 == 0:
        print(f"{number} even and divisible by 5")
    elif number % 2== 0:
        print(f"{number} even and not divisible by 5")
    elif number % 5 == 0:
        print(f"{number} odd and divisble by 5")
    else:
        print(f"{number} odd and not visible by 5")
