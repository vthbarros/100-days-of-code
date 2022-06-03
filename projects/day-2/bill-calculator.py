print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to slipt the bill? "))

total_bill_plus_tip = (tip/100) * total_bill + total_bill
bill_per_person = total_bill_plus_tip/number_of_people
bill_per_person = round(bill_per_person, 2)

print(f"Each person should pay: ${bill_per_person}")
