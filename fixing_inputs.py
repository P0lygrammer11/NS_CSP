#NS, fixing user inputs

while True:
    color = input("whats your favorite color? ").strip().lower()
    if color.isnumeric():
        print("That is not a color!")
    elif " "in color:
        print("I said one word.")
    else:
        break
    

print(f"we painted the walls {color}!")