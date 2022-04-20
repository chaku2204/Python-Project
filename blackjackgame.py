import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

repeat  = True

while repeat:
    ay = random.choice(cards)
    by = random.choice(cards)
    dd = random.choice(cards)
    ed = random.choice(cards)
    your_cards = [ay,by]
    delar_cards = [dd,ed]
    print(f"your cards : {your_cards}")
    print(f"delar cards: {delar_cards[0]}")

    in_game = True
    sum_y = 0
    sum_d = 0
    while in_game and sum_y < 22:
        get_another_card = input("Do you want to get another card type y or n ")
        if get_another_card == "y":
            cy = random.choice(cards)
            if cy == 11:
                if sum(your_cards) > 10:
                    cy = 1
            your_cards.append(cy)
        else:
            in_game = False
        sum_y = sum(your_cards)
        sum_d = sum(delar_cards)
        print(f"your cards : {your_cards}")
        print(f"your sum : {sum_y}")
        print(f"delar cards : {delar_cards}")
        print(f"delar sum: {sum_d}")

    while sum_d < 17:
        fd = random.choice(cards)
        if fd == 11:
            if sum(your_cards) > 10:
                fd = 1
        delar_cards.append(fd)
        sum_d = sum(delar_cards)

    print(f"delar cards : {delar_cards}")
    print(f"delar sum : {sum_d}")

    if sum_d < 22 and sum_y <22 :
        if sum_y < sum_d:
            print("you lose")
        elif sum_y > sum_d:
            print("you win")
        else:
            print("draw")
    elif sum_d < 22 and sum_y > 21:
        print("you lose")
    elif sum_d > 21 and sum_y < 22:
        print("you win")
    else :
        print("draw")

    ask = input("Do u want to repeat Y or N ")
    if ask == "n" :
        repeat = False



