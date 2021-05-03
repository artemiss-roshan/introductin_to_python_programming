def prog1():
    x = int(input("enter first number:"))
    y = int(input("enter second number:"))
    results=[]
    for i in range(x, y+1):
        if i%2==0:
            results.append(i)
    print( results)

prog1()        