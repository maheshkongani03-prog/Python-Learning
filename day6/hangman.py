import random
from hangman_art import stages,logo
from hangman_words import word_list
print(logo)
word_choice=random.choice(word_list)
placeholder='-'*len(word_choice)
print(f"word to guess:{placeholder}")
gameover=False
correct_letters=""
lives=6
while not gameover:
    display=""
    print(f"******You have {lives}/6 lives left*******")
    guess=input("Guess a Letter:").lower()
    if guess in correct_letters:
        print(f"you have already guessed {guess}")
    for letter in word_choice:
        if letter==guess:
            display+=letter
            correct_letters+=guess
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    if guess not in word_choice:
        print(f"the letter {guess} not in the word.You lose a life")
        lives-=1
    if lives==0:
        print("All your lives are Over")
        print(f"The Correct Word is {word_choice}.You lose")  
        gameover=True
    print(display)
    if "_" not in display:
        gameover=True
        print(f"The correct word in {word_choice}")
        print("You win")
    print(stages[lives])