import random 
words=["Iphone","Laptop","Books","Galaxy","World"]
def Hangman():
    word=random.choice(words).upper()
    Blankspaces=["_"]*len(word)
    incorrect_guesses=0
    max_incorrect_guesses=6
    while incorrect_guesses< max_incorrect_guesses and "_"in Blankspaces:
        print(" ".join(Blankspaces))
        Guess=input("Guess the letter:").upper()
        if len(Guess) != 1:
            print("Kindly  guess one letter at a time")
            continue
        if Guess in word:
            for i , letter in enumerate(word):
                if letter==Guess:
                    Blankspaces[i]=Guess
        else:
            incorrect_guesses+=1
            print(f"Incorrect!, You are left with {max_incorrect_guesses- incorrect_guesses} guesses")
                    
    if "_" not in Blankspaces:
        print("Congratulations,You won!!\nThe word is :")
        print(" ".join(Blankspaces))
    else:
        print(f"Sorry!,You lost. The word was {word}.")
Hangman()