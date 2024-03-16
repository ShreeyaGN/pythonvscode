weight = float(input("enter the weight: "))
height = float(input("enter the height : "))
bmi = weight / (height * height)
print(bmi)
if (bmi < 18.5):
    print("u r underweight")
elif (18.5 < bmi < 25):
    print("normal weight")
elif (25 < bmi < 30):
    print("slightly overweight")
elif (30 < bmi < 35):
    print("obese")
else:
    print("clinically obese")
    
    