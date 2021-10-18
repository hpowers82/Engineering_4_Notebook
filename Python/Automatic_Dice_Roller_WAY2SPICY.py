from random import randint

selectionvar="c"
# chooses which "mode" the dice roller is in
# if it is = to c, it prompts you to choose whether you want to edit the dice individually, or otherwise, how many dice you want to oll and how many sides you want each dice to have
dicenumb=0
# added to number automatically generated dice. basically just gets added up one each repitition, and is then thrown in the print command in order to label each dice roll. 
dicecust=1
# i would hypothetically use this in order
custSide=0
print ("Automatic Dice Roller")
diceList=[]
while selectionvar !="x": #if you select x when it prompts you to, it shuts down the program.
    if selectionvar == "c":# this makes the program choose between 
        print ("Type how many dice you want to roll, then press enter.")
        d=input("")
        print ("if you want to enter the values of each dice individually, press i, then enter. Otherwise, press enter")
        ind=input("")
        if ind != "i":
            print ("Type how many sides you want each dice to have, then press enter.")
            s=input("")
            print("rolling %s dice with %s side(s)!" % (d,s))
            for x in range (0,int(d)):
                dicenumb += 1
                print("Dice # %s is...%s!" % (dicenumb,randint(1,int(s))))
            dicenumb=0
        else:
            for x in range (0,int(d)):
                custSide=input("how many sides would you like dice # " +str(dicecust) +" to have?")
                dicecust += 1
                diceList.append(custSide)
            dicecust = 0
            for x in range (len(diceList)):
                print("Dice number " +str(dicecust)+" is "+str(randint(1,int(diceList[dicecust]))))
                dicecust += 1
            dicecustom = 0    
    print("Press enter to roll, c then enter to change the amount of dice and sides, or x then enter to exit!")
    selectionvar=input("")
