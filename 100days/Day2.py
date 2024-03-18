from art import tip

print(tip)
print("Welcome to the tip calculator.")
base_bill = float(input("Please enter bill amount: $"))
tip_percentage = float(input("Please enter your tip percentage: "))
tip_amount = round(base_bill * (tip_percentage / 100), 2)
total_bill = base_bill + tip_amount
print(f"The total bill is ${total_bill}. The tip amount is ${tip_amount}.")
num_people = int(input("How many people to split the bill? "))
per_person = round(total_bill / num_people, 2)
print(f"Each person should pay: ${per_person}")
