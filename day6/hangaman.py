import random  
import hangman_words
from hangman_art import stages,logo
print(logo)
word_choice=random.choice(hangman_words.word_list)
placeholder='-'*len(word_choice)
print(word_choice)
print(f"word to guess:{placeholder}")
gameover=False
correct_letters=""
lives=6
while not gameover:
    print(F"********YOU HAVE {lives}/6 LIVES LEFT********")
    display=""
    guess=input("guess a letter:").lower()
    if guess in correct_letters:
        print(f"yoou have already guessed {guess}!!!!!!")
    for char in word_choice:
        if guess==char:
            display+=guess
            correct_letters+=guess
        elif char in correct_letters:
            display+=char
        else:
            display+="_"
    if guess not in word_choice:
        print(f"you guess {guess},thats not in the word.You lose a Life")
        lives-=1
    if lives==0:
        print("ALL your lives are over")
        print(f"The Correct Word is {word_choice}.You lose")  
        gameover=True
    print(display)
    if '_' not in display:
          gameover=True
          print("you win")
    print(stages[lives])
    
            
    

        


        

