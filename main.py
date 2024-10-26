import random


def deal_card():
    """Returns a randorm card from the deck"""
    cards = [11, 2, 3, 4,5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

    
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!!!"
    elif user_score > 21:
        return "You went over, you lose!"
    elif computer_score > 21:
        return "opponent went over, you win!!!"
    elif user_score > computer_score:
        return "You win!!!"
    else:
        return "You lose!"

user_cards = []
computer_cards = []
computer_score = -1
user_score = -1
is_game_over = False

for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    
    computer_cards.append(deal_card())
    
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
      
    return sum(cards)

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input(":Type 'y' to get another card, type 'n' to pass: ") 
        if user_should_deal == "y":
             user_cards.append(deal_card())
        else:
            is_game_over = True   
            
while computer_score != 0 and computer_score < 17:
    computer_score.append(deal_card())
    computer_score = calculate_score(computer_cards)   
      
print(compare(user_score, computer_score))