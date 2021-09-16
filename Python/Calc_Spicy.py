print("Calculator Program")
repeat=0
a = int(input("Enter your first number:"))
b = int(input("Enter your second number"))
def doMath(a,b,c):
    numbA = a #variables 
    numbB = b
    productA = a
    productB = b
    if c == 1:
        return str(a+b)
    if c == 2:
        return str(a-b)
    if c == 3:
        return str(a*b)
    if c == 4:
        return str(a/b)
    if c == 5:
        return str(a%b)
    if c == 6:
        numbA = numbA - 1 #sets numbA into one less than A for the biginning, only once.
        while numbA != 1: #makes it not go infinately/go negative
            productA=productA*numbA
            numbA = numbA - 1
        return(str(productA))
    if c == 7:
        numbB = numbB - 1
        while numbB != 1:
            productB=productB*numbB
            numbB = numbB - 1
        return(str(productB))
#while repeat!="x"

print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
print("1st Factorial:\t" + doMath (a,b,6))
print("2nd Factorial:\t" + doMath (a,b,7))
