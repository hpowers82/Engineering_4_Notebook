from random import randint

stop="c"
dicenumb=0

print ("Automatic Dice Roller")

while stop !="x":
    if stop == "c":
        print ("How many dice?")
        d=input("")
        print ("How many sides?")
        s=input("")
        print("rolling %s dice with %s side(s)!" % (d,s))
    for x in range (0,int(d)):
        dicenumb += 1
        print("Dice # %s is...%s!" % (dicenumb,randint(1,int(s))))
    dicenumb=0
    print("Press enter to roll, c then enter to change the ammount of dice, or x then enter to exit!")
    stop=input("")


