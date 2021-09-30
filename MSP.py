

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
counter = 0
mistakeCount = 0
hits=""
misses = ""
wordTrue = input ("Player 1, please enter your word.\n")
while " " in wordTrue:
    wordTrue = input("The input must be one word.")
word = [char for char in wordTrue]
print(word)
dashes = ("_") * len(word)
goodInput = True
print("\n"* 50)
guessIndex=0
correctList=""
counter = 0
hitCount = 0
prettyDash =" ".join(dashes)
while True:
    MSP(mistakeCount)
    print("\n")
    
    print(prettyDash+"\n")
    
    print("mistakes left: " + str(7-mistakeCount) + "\n")
    
    if misses != "":    
        print("mistakes made: " + ", ".join(misses))
        
    guess = input("Player 2, please enter a letter to guess. \n")
    
    print("\n"*50)

    if len(guess) > 1:
        print("please only guess one charecter.")
        goodInput = False
    
    if guess in hits: 
        print("You have already guessed that letter. please guess again.")
        goodInput = False
    
    if guess in misses: 
        print("You have already guessed that letter. please guess again.")
        goodInput = False
        
    if goodInput == True:
        if guess in word:
            print(guess + " is correct!")
            hits = hits + guess
            hitCount = hitCount + 1
            
        else:
            print(guess + " is not correct!")
            misses = misses + guess
            mistakeCount += 1
            goodInput = False
            

        while counter != len(word):
            
            if word[counter] == guess:
              dashes = dashes[:counter] + word[counter]+ dashes[counter+1:]
            counter += 1
            
        counter = 0
        
        prettyDash = " ".join(dashes)
    goodInput = True
    if wordTrue == dashes:
        print("Yes! the answer is "+wordTrue)
        print("found with " + str(mistakeCount) + " missed guesses and " + str(hitCount) + " correct guesses.")
        break
    
    if mistakeCount > 6:
        print("You have run out of guesses!")
        print("You used " + str(mistakeCount) + " missed guesses and " + str(hitCount) + " correct guesses.")
        print("The word was " + wordTrue)
        break
