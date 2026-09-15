#NS, hello user

while True:
    name = input("Hi, whats your name? ").strip().title()
    if name.isnumeric():
        print("please type in letters!")
    elif " "in name:
        print("Please only enter first name!")
    else:
        break

print(f"Hello {name}!")