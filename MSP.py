word=input("Player 1, please type your word and press enter.\n")
dashnumb=0
mistakes=0
def split(word):
    return [char for char in word]
print("\n" * 50)

def MSP(mistakes):
    print("---┐")
    if mistakes > 0:
        print("   O ")
    if mistakes == 2:
        print("   |")
    if mistakes == 3:
        print("  \|")
    if mistakes > 3:
        print("  \|/")
    if mistakes > 4:
        print("   |")
    if mistakes == 6:
        print("  /")
    if mistakes > 6:
        print("  / \ ")
set
MSP(mistakes)
print("\n\n\n")
print (dashes)
def asker(split,word,dashes):
    guess=input("Player 2, please enter your guess.\n")
    if guess in split(word):
        print("wow you got it wowowcool")
        ll=word.index(guess)
        dashes[ll]=guess 
        print(dashes)
    elif guess not in splint(word):
        print("booocringe")
asker(split,word,dashes)
