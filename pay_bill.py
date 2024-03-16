#random person from the grp will have to pay the food bill
import random

names = ["shriya" , "raji" , "guru" , "subbu" , "sanju"]
num_of_items = len(names)
#print(len(names))
random = random.randint(0, num_of_items)
persontopay = names[random]
print(f"{persontopay} has to pay the bill")
