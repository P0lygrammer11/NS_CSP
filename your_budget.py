# NS, your budget

income = float(input("Whats your monthly income? "))
rent = float(input("what your monthly rent/mortgage? "))
utilities = float(input("what is your monthly utilities? "))
groceries = float(input("What is your monthly groceries? "))
transportation = float(input("What is your monthly transportation? "))

rent_1 = int(round((rent / income) * 100))
utilities_1 = int(round((utilities / income) * 100))
groceries_1 = int(round((groceries / income) * 100))
transportation_1  = int(round((transportation / income) * 100))

savings = income * 0.10
saving_1 = 10

spending_money = income - rent - utilities - groceries - transportation - savings

print(f"your rent  is ${rent} and that is {rent_1} % of your income.")
print(f"your utilities cost ${utilities} and that is {utilities_1} % of your income.")
print(f"your groceries is ${groceries} and that is {groceries_1} % of your income.")
print(f"you transportation is ${transportation} and that is {transportation_1} % of your income.")
print(f"your should save ${savings} and that {saving_1} % of your income.")
print(f"${spending_money} is your spending money.")
