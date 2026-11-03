import game_data
import random  
def is_correct(fa,fb,choice1):
    if fa>fb:
        return choice1=="a"
    else:
        return choice1=="b"
random_number2 = random.randint(0, 49)
score=0
sh=True
while sh:
    random_number1=random_number2
    random_number2=random.randint(0, 49)
    while True:
        
        if random_number2 != random_number1:
            break
    choice1=game_data.data[random_number1]
    print(f"compare A: {choice1['name']}, {choice1['description']}, {choice1['country']}")
    choice2=game_data.data[random_number2]  
    print(f"against B: {choice2['name']}, {choice2['description']}, {choice2['country']}")
    followers1=game_data.data[random_number1]['follower_count']
    followers2=game_data.data[random_number2]['follower_count']
    print(f"1:{followers1}, 2:{followers2}")
    choice=input("Who has More Followers 'A' or 'B':").lower()
    final=is_correct(followers1,followers2,choice)
    if final:
        score+=1
        print(f"you got it Correct current score:{score}")
    else:
        print(f"you got it wrong {score}")
        sh=False



