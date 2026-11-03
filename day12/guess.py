import random
print("Welcome to the Number Guessing Game!!")
print("I am thinking a number between 1 and 100")
number=random.randint(1,100)
print(f"the number is {number}.")
def mode():
    difficulty=input("Choose  a difficulty level 'Easy' or 'Hard':").lower()
    if difficulty=='easy':
        chances=5
    else:
        chances=10
    return chances
def game():
        chances=mode()
        game_over=False
        while chances>0:
            print(f"you have {chances} chances to find the number!")
            make_a_guess=int(input("Make a Guess:"))
            if make_a_guess==number:
                chances=0
                print("you are right")
            elif make_a_guess<number:
                print( "too low")
                chances-=1
            else:
                print("too high")
                chances-=1
        if chances==0:
             print("Game Over")
game()

    


