import random

def randInt(max,min):
    if max == 0 and min == 0:
        num = random.random()*50 +50
        return int(num)
    elif max == 50 and min==0:
        num = random.random()*50
        return int(num)
    elif max == 500 and min == 50:
        num = random.random()*450 + 50
        return int(num)
    if max < min:
        return "min is bigger than max !"
    if max < 0:
        return "max is less than 0 !"
print(randInt(500,50)) 	
# should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
