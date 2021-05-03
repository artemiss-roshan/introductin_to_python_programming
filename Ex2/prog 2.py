def prog2():
    x = int(input("enter first number:"))
    y = int(input("enter second number:"))
    result = []
    for i in range(min(x, y)+1, max(x, y)):
        if i%2==0:
            result.append(i)
    print( result)

prog2() 