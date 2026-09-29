#Ns, Caesar Cipher

choice = input("would you like to (E)Encrypt or (D)Decrypt a message? ")
message = input("what is your message? ")
shift = input("enter a sift amount: ")

def caesar_shift(message, shift):
    result = ""
    for char in message:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


if choice == 'E':
    encrypted = caesar_shift(message, shift)
    print(f"Your encrypted message is: {encrypted}")
elif choice == 'D':
    decrypted = caesar_shift(message, - shift)
    print(f"Your decrypted message is: {decrypted}")
