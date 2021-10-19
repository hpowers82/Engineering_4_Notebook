def MSP(mistakeCount):
    print("---┐")
    if mistakeCount > 0:
        print("   O ")
    if mistakeCount == 2:
        print("   |")
    if mistakeCount == 3:
        print("  \|")
    if mistakeCount > 3:
        print("  \|/")
    if mistakeCount > 4:
        print("   |")
    if mistakeCount == 6:
        print("  /")
    if mistakeCount > 6:
        print("  / \ ")
repeatVar=""
while repeatVar !="x":
    counter = 0 #counter is a variable that i use to cycle through a list in order to check every element in it.
    
    mistakeCount = 0 #mistakeCount is the count of wrong letters you enter.
    
    
    hitCount=0 #the number of correct guesses.
    hits="" #hits is a list of all the correct guesses you have made
    
    misses = "" #misses is a list of all the incorrect guesses you have made.
    
    word = input ("Player 1, please enter your word.\n")
    
    while " " in word: #makes sure that the word is one phrase
        word = input("The input must be one word.")
    
    print("\n"* 50)
    
    wordList = [char for char in word] #word is a list of the individual letters in the word
        
    dashes = ("_") * len(wordList) #dashes is a list that has the same number of dashes as letters in the word, and is changed in order to be displayed.
    
    goodInput = True #goodInput decides whether the guess should count as an actual guess.
    
    hitCount=0 #the number of correct guesses.
    
    print("\n"* 50)
                    
    prettyDash =" ".join(dashes) #
    
    repeatVar="" #decides whether or not to repeat the game. if it is equal to x, ends everything.
    
    while True:
        MSP(mistakeCount)
        print("\n")
        
        print(" ".join(dashes)+"\n")
        
        print("mistakes left: " + str(7-mistakeCount) + "\n")
        
        if misses != "":    
            print("mistakes made: " + ", ".join(misses))
            
        guess = input("Player 2, please enter a letter to guess. \n")
        
        print("\n"*50)
    
        if len(guess) > 1:
            print("please only guess one charecter.")
            goodInput = False
        
        if guess in hits or guess in misses: 
            print("You have already guessed " + guess + ".")
            goodInput = False
        
        #if guess in misses: 
          #  print("You have already guessed " + guess +" . please guess again.")
            #goodInput = False
            
        if goodInput == True:
            if guess in wordList:
                print(guess + " is correct!")
                hits = hits + guess
                hitCount = hitCount + 1
                
            else:
                print(guess + " is not correct!")
                misses = misses + guess
                mistakeCount += 1
                goodInput = False
                
    
            while counter != len(wordList):
                
                if wordList[counter] == guess:
                  dashes = dashes[:counter] + wordList[counter]+ dashes[counter+1:]
                counter += 1
                
            counter = 0
            
            prettyDash = " ".join(dashes)
        goodInput = True
        if word == dashes:
            print("Yes! the answer is "+word)
            print("found with " + str(mistakeCount) + " missed guesses and " + str(hitCount) + " correct guesses.")
            break
        
        if mistakeCount > 6:
            print("You have run out of guesses!")
            print("You used " + str(mistakeCount) + " missed guesses and " + str(hitCount) + " correct guesses.")
            print("The word was " + word)
            break
        goodInput=True
    repeatVar=input("Press enter to play again, or press x and then enter to quit.")
