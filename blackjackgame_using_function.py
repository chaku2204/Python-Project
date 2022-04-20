import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def card():
    return random.choice(cards)

def sum_card(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(your_score, computer_score):
    if your_score == computer_score:
        return "draw"
    elif your_score == 0:
        return "you win"
    elif computer_score == 0:
        return "you lose"
    elif your_score < 22 and computer_score > 22:
        return "you win"
    elif your_score > 22 and computer_score < 22:
        return "you lose"
    elif your_score > computer_score:
        return "you win"
    else:
        return "you lose"
    
def play_game():
    your_cards = []
    delar_cards = []

    for i in range(2):
        your_cards.append(card())
        delar_cards.append(card())


    game_is_over = False
    while not game_is_over:
        your_score = sum_card(your_cards)
        computer_score = sum_card(delar_cards)
        
        if your_score == 0:
            print(f"your cards : {your_cards}. your score : 21")
        else:
            print(f"your cards : {your_cards}. your score : {your_score}")

        print(f"delar first card : {delar_cards[0]}")

        if your_score == 0 or computer_score == 0 or your_score > 21:
            game_is_over = True
        else:
            ask = input("Do you want to add another cards: y or n ")
            if ask == "y":
                your_cards.append(card())
            else:
                game_is_over = True

    while computer_score!=0 and computer_score < 17:
        delar_cards.append(card())
        computer_score = sum_card(delar_cards)

    print(f"your final cards : {your_cards}. your final score: {your_score}")
    print(f"computer final card : {delar_cards}.delar final score: {computer_score}")

    print(compare(your_score, computer_score))

play_game()

while  input("Do you want to play more y or n") == "y":
    play_game()


