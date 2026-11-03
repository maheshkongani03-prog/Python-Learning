import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
    
def calculate_score(cardss):
    if sum(cardss)==21 and len(cardss)==2:
        return 0
    if 11 in cardss and sum(cardss)>21:
        cardss.remove(11)
        cardss.append(1)
    return sum(cardss)
def compare(user_score, computer_score):
    # Bug fix. If you and the computer are both over, you lose.
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
def play_game():
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1
    is_game_over=False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_cards)
        cmp_score=calculate_score(computer_cards)
        print(f"your cards: {user_cards}, current score: {user_score},")
        print(f"computer's first card: {computer_cards[0]}")
        if user_score==0 or cmp_score==0 or user_score>21:
            is_game_over=True
        else:
            user_choice=input("type 'y' to deal, 'n' to pass:")
            if user_choice=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))

t=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") 
while t=='y':
    play_game()
    print("\n"*20)
   
    


        