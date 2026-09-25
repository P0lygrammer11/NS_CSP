#NS, loops notes

import random
ducks = 1
goose = random.randint(1,11)
while True:
    if ducks == goose:
        break
    print("duck......")
    ducks += 1
print("GOOSEEEEEEEEEEEEEEEEE. ")

sibling = ["Alex", "Katie" , "Nari"]
print(sibling[2])
sibling.append("jayshree")
sibling.insert(3,"vienna")
print(sibling)
sibling.pop(4) #if you dont give it a numbr itll just take out the last one in the list
print(sibling)
#for loops
for num in range(1,25):
    if num % 15 == 0:
        print("FIZZBUZZ")
    elif num % 3 == 0 :
        print("frizz")
    elif num % 5  == 0:
        print("buzz")
    else:
        print(num)


    #range builts a list for you, you can even tell it to what to count by
for sibling in sibling :
    print(sibling)
    