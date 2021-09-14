
# Automatic Dice Roller

# Written by Hank Powers

from random import randint
print ("Automatic Dice Roller")
n=input("Press enter to roll!")
#print(n)
if n=="":
    print("Your number is...%s!" % randint(1,6))
#n=input("Press enter to roll, or press x to exit!")
#print(n)
while n !="x":
   print("Press enter to roll, or x to exit!")
   n=input("")
   print("Your number is...%s!" % randint(1,6))

    
    
