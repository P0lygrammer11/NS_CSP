#NS, Functions notes
def stupit_proof(money):
    while True:
        try:
            amount = float(input(f"what is your montholy {money }: "))
            return amount
        except:
            print("this isnt a number:( ")

income = stupit_proof("income")
rent = stupit_proof("rent")
utilities = stupit_proof("utilities")
grocceries = stupit_proof("grocceries")
transportation = stupit_proof("transportation")


#write your variables
income = float(input("what is your monthloy income? "))
rent = float(input("what is your monthloy rent? "))
utilities = float(input("what is your monthloy utilities? "))
grocceries = float(input("what is your monthloy grocceries? "))
transportation = float(input("what is your monthloy transportation? "))
saving = income*0.1
#write any functions your using
def calc_precent(income, bill):
    return round(bill/income*100)

#outputs for the user
print(f"your rent is ${rent:.2f} that is {calc_precent(income, rent)}% of your income")
print(f"your utilities is ${utilities:.2f} that is {calc_precent(income, utilities)}% of your income")
print(f"your grocceries is ${grocceries:.2f} that is {calc_precent(income, grocceries)}% of your income")
print(f"your transportation is ${transportation:.2f} that is {calc_precent(income, transportation)}% of your income")
print(f"your should save ${saving:.2f} that is {calc_precent(income, saving)}% of your income")
print(f"you have ${income-rent-utilities-grocceries-transportation-saving:.2f} left to spend")





