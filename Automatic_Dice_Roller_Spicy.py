'''
                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
'''

from random import randint
print ("Automatic Dice Roller")
print ("How many dice?")
d=input("")
print ("How many sides?")
s=input("")
stop=0
while stop !="x":

   # print("Press enter to roll, or x to exit!")
   # n=input("")
    for x in range (0,int(d)):
        print("Your number is...%s!" % randint(1,int(s)))
    print ("Press enter to roll, c then enter to change the ammount of dice, or x then enter to exit!")
    stop=input("")
    if stop == "c":
        print ("How many dice?")
        d=input("")
        print ("How many sides?")
        s=input("")

