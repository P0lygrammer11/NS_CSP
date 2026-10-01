#Ns, Caesar Cipher

choice = input("Would you like to (E)encrypt or (D)decrypt a message? ").strip().capitalize()
message = input("Enter your message: ").strip()
shift = int(input("Enter shift amount: ").strip()


def caesar_shift(message, shift):
    the_result = ""
    for char in message:
        if char.isupper():
            the_result += (
                chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            )
        elif char.islower():
            the_result += (
                chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            )
        else:
            the_result += char
    return the_result


if choice == "E":
    the_result = caesar_shift(message, shift)
    print(f"Your encrypted message is: {the_result}")

elif choice == "D":
    the_result = caesar_shift(message, -shift)
    print(f"Your decrypted message is: {the_result}")


