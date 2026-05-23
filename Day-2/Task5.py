print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? ₹"))
tip = int(input("What percentage tip would you like to give? 10 12 15 :"))
people = int(input("How many people to split the bill? "))
Add_Tip = bill * tip / 100 + bill
Add_People = Add_Tip / people
total_bill = Add_People
print (f"Each person should pay : ₹{total_bill}")
