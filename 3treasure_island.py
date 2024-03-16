print("welcome to treasure island, ur mission is to find treasure")
d1 = input("chose 'left' or 'right' ")
if d1 == "left":
    d2 = input("chose 'swim' or 'wait' ")
    if d2 == "wait":
        d3 = input("which door? 'yellow' or 'red' or 'blue' ")
        if d3 == "yellow":
            print("u win")
        elif d3 == "red":
            print("burnt by fire, game over")
        else:
            print("game over")
    else:
        print("attacked by trout, game over")
else:
    print("fell into a hole, game over")
    

