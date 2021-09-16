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
print("rolling %s dice with %s side(s)!" % (d,s))
stop=0
dicenumb=0
while stop !="x":
    for x in range (0,int(d)):
        dicenumb += 1
        print("Dice # %s is...%s!" % (dicenumb,randint(1,int(s))))
    dicenumb=0
    print("Press enter to roll, c then enter to change the ammount of dice, or x then enter to exit!")
    stop=input("")
    if stop == "c":
        print ("How many dice?")
        d=input("")
        print ("How many sides?")
        s=input("")
        print("rolling %s dice with %s side(s)!" % (d,s))
