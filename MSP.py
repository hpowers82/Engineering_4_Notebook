

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

word = [char for char in wordTrue]
print(word)
dashes = ("_") * len(word)

print("\n"* 50)
guessIndex=0
correctList=""
counter = 0
x=
hitCount = 0
prettyDash =" ".join(dashes)
while True:
    MSP(mistakeCount)
    print("\n")
    
    print("prettyDash\n")
    
    print("mistakes left: " + str(mistakeCount) + "\n")
    
    if misses != "":    
        print("mistakes made: " + ", ".join(misses))
    guess = input("Player 2, please enter a letter to guess. \n")
    if len(guess) > 1:
        print("please only guess one charecter.")
        continue
    if guess in hits: 
        print("You have already guessed that letter. please guess again.")
        continue
    if guess in misses: 
        print("You have already guessed that letter. please guess again.")
        continue
    if guess in word:
        hits = hits + guess
        hitCount = hitCount + 1
    else:
        print("Nope, try again!")
        misses = misses + guess
        mistakeCount += 1
        continue
    while counter != len(word):
        if word[counter] == guess:
          dashes = dashes[:counter] + word[counter]+ dashes[counter+1:]
        counter += 1
    counter = 0
    prettyDash = " ".join(dashes)
    if wordTrue == dashes:
        print("Yes! the answer is "+wordTrue)
        print("found with" +mistakeCount +"missed guesses and "+hitCount+ "correct guesses.")
        break
    if mistakeCount > 7:
        print("You have run out of guesses!")
        print("You used" + mistakeCount +"missed guesses and "+hitCount +"correct guesses.")
        print("The word was" + wordTrue)
        break
