#create a empty set and a empty dictinary. 
#append the dictinary with the name as key and scores as values. 
#now append the names(keys) with scores more than 90 to the set. 

s = set()
d = {}
size = int(input("enter the num of records:"))
for i in range(size):
    
    name = input("enter the names")
    score = float(input("enter the scores:"))
    d.update({name:score})
print (d)

for key,val in d.items():
        if val > 90:
            s.add(key)
            s.add(val)
            print(s)


 