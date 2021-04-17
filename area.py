def area(a, b, c, d ,dd):
    if d == 0 :
        s = (a + b + c) / 2
        return ((s*(s-a)*(s-b)*(s-c)) ** 0.5)
    else:
        s1 = (a + b + dd) / 2        
        s2 = (c + d + dd) / 2
        return (((s1*(s1-a)*(s1-b)*(s1-dd)) ** 0.5)+((s2*(s2-c)*(s2-d)*(s2-dd)) ** 0.5))
        
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
d = float(input('Enter third side: '))
dd = float(input('Enter diameter: '))

print ("area= ",(area(a, b, c, d, dd)))