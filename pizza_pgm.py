print("Thank u for chosing python pizza deliveries")
bill = 0
size = input("enter 's' for small, 'm' for medium and 'l' for large :")
add_pepp = input("if u want pepp then 'Y' or 'N' ")
extra_cheese = input("if u want extra cheese then 'Y' or 'N' ")
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25
    
if add_pepp == "Y":
    if size == "s":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"ur final bill is {bill}")
        
    