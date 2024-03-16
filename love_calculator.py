print("welcome to love calculator")
print("we are calculating ur love score")
frst_name = input ("enter the frst name:")
sec_name = input("enter the sec name: ")
combined = (frst_name + sec_name).lower()
t = combined.count("t")
r = combined.count("r")
u = combined.count("u")
e = combined.count("e")
frst_digit = t + r + u + e

l = combined.count("l")
o = combined.count("o")
v = combined.count("v")
e = combined.count("e")

sec_digit = l + o + v + e

score = str(frst_digit) + str(sec_digit)
print(score)

