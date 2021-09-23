word=input("Player 1, please type your word and press enter.")

letters = []
print("\n" * 50)
mistakes=0

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
#print("asdfad" + MSP(7))
print()
MSP(mistakes)
def asker():
    guess=input("Player 2, please enter your guess.\n")
