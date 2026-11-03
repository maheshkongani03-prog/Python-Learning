import random
def deal_cards():
    cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)
def calculate_score(cardss):
    if sum(cardss)==21 and len(cardss)==2:
        return 0
    if 11 in cardss:
        cardss.remove(11)
        cardss.append(1)
    return sum(cardss)
    
    
user_cards=[]
comp_cards=[]
for i in range(2):
    user_cards.append(deal_cards())
    comp_cards.append(deal_cards())
    is_game_over=False
    while not is_game_over:
        user_score=calculate_score(user_cards)
        comp_score=calculate_score(comp_cards)




    
