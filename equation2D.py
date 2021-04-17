def Equation2D (a, b, c):
    d = b*b-4*a*c
    if d == 0 :
        return (-b/2*a)
    else:
        if d< 0 :
            return ("no answer")
        else:
            return ((-b+((b**2-4*a*c)**0.5)/2*a) , (-b-((b**2-4*a*c)**0.5))/2*a)
                    
a = float(input('a=:'))
b = float(input('b=:'))
c = float(input('c=:'))

print ("answer(s) ",(Equation2D(a, b, c)))