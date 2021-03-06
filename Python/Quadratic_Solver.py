from math import sqrt
x=""
def doMath(a,b,c):
    disc = (b**2) - (4*a*c)# the discriminant tells you how many roots there are. 
    if disc > 0: #if it is greater than 0, there are two for a quadratic.
        root1=(-b + sqrt(b**2-4*a*c))/(2*a)
        root2=(-b - sqrt(b**2-4*a*c))/(2*a)
        roots = [root1,root2]
    elif disc == 0: #if it is 0, there is one root.
        root1 = (-b + sqrt(b**2-4*a*c))/(2*a)
        roots = root1
    elif disc < 0: #if it is less than 0, there are none.
        roots= ""
    return roots #sends roots out of the function, to be called fore later
while x != "x":
    print("Quadratic Solver")
    print("Enter the coefficients for ax^2 + bx + c = 0")
    
    print("Enter coefficient a")
    a=int(input(""))
    
    print("Enter coefficient b")
    b=int(input(""))
    
    print("Enter coefficient c")
    c=int(input(""))
    print("You entered %dx^2 +%dx + %d = 0" % (a,b,c))
    roots = doMath(a,b,c)
    h=(-b)/(2*a)
    k=a*(h**2)+b*h+c
    if len(roots) == 0: # len measures the amount of elements in a range. therefore, if there are none, there are no roots.
        print("There are no real roots")
    else: 
        print("Root #1: ")#there has to be at least one root if there are any (duh)
        print(roots[0])
        if len(roots) == 2:
            print (roots[1])
        print("Vertex form: %g(x-%g)^2+%g" % (a,h,k))
    print("Press Enter to run again, or press x then Enter to quit")
    x=input("")
