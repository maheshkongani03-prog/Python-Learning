import random
data = ["rock", "paper", "scissors"]
user_random_number=int(input("what is your choice:"))
user_choice = data[user_random_number]
comp_random_number = random.randint(0, 2)
comp_choice = data[comp_random_number]
print(f"user choice: {user_choice}")
print(f"comp choice: {comp_choice}")
if user_random_number>2 or user_random_number<0:
    print("Invalid.you lost")
elif user_random_number == comp_random_number:
    print("Draw")
elif (user_random_number == 0 and comp_random_number == 2):
    print("You win")
elif (user_random_number == 2 and comp_random_number == 0):
    print("You lose")
elif user_random_number > comp_random_number:
    print("You win")
elif user_random_number < comp_random_number:
    print("You lose")
