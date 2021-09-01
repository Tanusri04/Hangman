import random
a=input("Enter your name: ")
print("Hi,",a,"!")
print('''Welcome to Hangman! You will get five chances to guess the correct word. 
If you guess it then you win! Good luck and enjoy :)''')
words = ['enthusiastic','plagiarism','jazz','zebra','nymph','gizmo','jukebox','fluffy','juicy']
gameword = random.choice(words)
guess = ''
chances=5
while chances>0:
    fails=0
    for ch in gameword:
        if ch in guess:
            print(ch)
        else:
            print("_")
            fails+=1
    if fails==0:
        print("You win! The word was indeed", gameword)
        break
    try_2=input("Guess the character of the word:")
    guess += try_2
    if try_2 not in gameword:
        chances-=1
        print("Wrong guess. Now, you have ",chances,"left")
        if chances==0:
            print("You have 0 chances left and you have lost the game ")
            print("The word was ",gameword)
    