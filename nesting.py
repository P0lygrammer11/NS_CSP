# NS, number information

for number in range(1,21):
    if number % 2 == 0:
        print(f"{number} is even and not divisible by 5")
        if number % 2== 0 and number % 5== 0:
            print(f"{number} is even and divisible by 5")
    elif number % 5== 0:
        print(f"{number} is odd and divisible by 5")
    else:
        print(F"{number} is odd and not divisble by 5")