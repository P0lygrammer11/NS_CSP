# NS, string notes

#strings => any saved inside the quotation marks "  " ' '
name = input("what is your name? ").strip().capitalize()
age = input('how old are you?')
print(type(age))

#concatenation => puts two strings directly nest to each other.
#print(age * age)

print(name + ' ' + 'larose')

sentence = "The quick brown fox jumped over the lazy dog."
print(sentence)
print(sentence.replace("dog" , "monkey"))
print(len(name)) #<= gets the lenghth of the strig
print = input(f"Your name is {name} that is {len(name)} letter long. youyr firrst intial is {name[0]}, i think i will call you {name[0:3]}")
#sting.action/method()
#strip removes spaces from the beginning and the end.
#f-string=> forward string lets you write code inside your string
# len tells you the lenghth of something
# index# is a specific number
#slice => a string pull put a smaller piece
