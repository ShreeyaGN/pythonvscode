def if_prime(num):
    factor = 0
    for i in range (1,num+1):
        if num % i == 0:
            factor = factor + 1
    if factor == 2:
        return True
    else:
        return False

n = int(input("Enter a number"))
for i in range (1, n+1):
    if if_prime(i) and if_prime(n-i):
        print(f"{n} = {i} + {n-i}")
        
