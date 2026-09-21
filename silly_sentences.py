#NS,p7 , silly sentenses
while True:
    adjective = input("eneter an adjective: ").strip().title()
    if adjective.isnumeric():
        print("please type in letters!")
    elif " "in adjective:
        print("Please only enter one adjective!")
    else:
        break

while True:
    color = input("eneter a color: ").strip().lower()
    if color.isnumeric():
        print("please type in letters!")
    elif " "in color:
        print("Please only 1 color!")
    else:
        break


while True:
    animal = input("an animal that you find cute: ").strip().lower()
    if animal.isnumeric():
        print("please type in letters!")
    elif " "in animal:
        print("please only 1 animal!")
    else:
        break


while True:
    ing = input(" a ver ending in -ing(action word): ").strip().lower()
    if ing.isnumeric():
        print("please type in letters!")
    elif " "in ing:
        print("Please only 1 verb!")
    elif not ing.endswith("ing"):
        print("please enter a verb ending in 'ing'")
    else:
        break

while True:
    noun = input("a silly noun: ").strip().lower()
    if noun.isnumeric():
        print("please type in letters!")
    elif " "in noun:
        print("Please only enter 1 noun!")
    else:
        break

while True:
    adjective_1 = input("eneter an adjective: ").strip().title()
    if adjective_1.isnumeric():
        print("please type in letters!")
    elif adjective == adjective_1:
        print("Please enter a different adjective!")
    else:
        break

print("Captain Sparkles steered the spaceship toward a "  + adjective + " new planet. As they landed, they noticed the alien sky was completely " + color + ". Suddenly, a giant " + animal +  " stepped out from behind a crater. It started " + ing +  " across the rocky ground right toward them! The alien creature handed the crew a tiny, glowing " + noun +  " and said, Welcome to our planet. We think humans are incredibly " + adjective_1 + "!")

