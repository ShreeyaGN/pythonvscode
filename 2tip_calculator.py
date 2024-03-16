#write a pgm to take bill as input and percentage amount as tip, number of people. calculate how much each will split in the final bill. 
print("welcome to tip calculator")
bill = float(input("enter the total bill:"))
tip = int(input("enter the tip you wud like to give: "))
people = int(input("enter the number of peoplr "))
bill_after_tip = (bill * tip) / 100
amount = bill_after_tip / people
print(f"each one will pay : {amount}. ")
