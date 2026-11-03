import random
import game_data
account_b=random.choice(game_data.data)
def check_answer(fa,fb,guess1):
    if fa>fb:
        return guess1=="a"
    else:
        return guess1=="b"
score=0
should_continue=True    
while should_continue:
    account_a=account_b
    account_b=random.choice(game_data.data)
    if account_b == account_a:
        account_b = random.choice(game_data.data)
    print(f"compare A:{account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print(f"Against B:{account_b['name']}, a {account_b['description']}, from {account_b['country']}")
    followers_a=account_a['follower_count']
    followers_b=account_b['follower_count']
    print(f"1:{followers_a},2:{followers_b}")
    guess=input("Who has More Followers 'A' or 'B':").lower()
    is_correct=check_answer(followers_a,followers_b,guess)

    if is_correct:
        score+=1
        print("you got it right")
            
    else:
        print(f"You got it wrong and your final_score is:{score}")
        should_continue=False
