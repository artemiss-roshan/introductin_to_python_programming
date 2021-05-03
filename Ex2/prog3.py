def prog3(x):
    num=0
    for i in range(1,x+1):
        if x%i==0:
            num+=1
    return num==2
print(prog3(1)) 