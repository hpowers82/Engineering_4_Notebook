print("Calculator Program")
repeat=0
a = int(input("Enter your first number:"))
b = int(input("Enter your second number")) #int is a number
def doMath(a,b,c): #import relevent variables: c decides what type of math you want to do.
    if c == 1:
        return str(a+b) #str makes the answer a phrase, not just a raw number
    if c == 2:
        return str(a-b)
    if c == 3:
        return str(a*b)
    if c == 4:
        return str(a/b)
    if c == 5:
        return str(a%b)

print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
