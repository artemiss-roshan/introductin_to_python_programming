import random
def Rand2 (a, b):
    if b>a:
        if a%2 == 0:
            return (random.randrange(a,b, 2))
        else:
            return (random.randrange(a+1,b, 2))
    else:
        if b%2 == 0:
            return (random.randrange(b,a, 2))
        else:
            return(random.randrange(b+1,a, 2))
        
a = int(input('a=:'))
b = int(input('b=:'))

print ("answer ",(Rand2(a, b)))