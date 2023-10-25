logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import subprocess
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def Add_player_card(score):
    if score == 0:
        for i in range(2):
            x=random.choice(cards)
            players_cards.append(x)
            score += x
    else:
        x=random.choice(cards)
        if x == 11 and score + x > 21:
            x = 1
        players_cards.append(x)
        score += x
    print(f"   Your cards: {players_cards}, current scores: {score}")
    return score

def Add_computer_card(score):
    if score == 0:
        for i in range(2):
            x=random.choice(cards)
            computers_cards.append(x)
            score += x
    else:
        while True:
            if score >= 20:
                break
            else:
                x=random.choice(cards)
                computers_cards.append(x)
                score += x
    return score

def Final(comp_score,play_score):
    print(f"Your final hand: {players_cards}, final score: {play_score}")
    comp_score = Add_computer_card(comp_score)
    print(f"Computer's final hand: {computers_cards}, final score: {comp_score}")
    if play_score == 21:
        print("You win!!")
    elif player_score > comp_score and play_score <= 21:
        print("You Win!!")
    elif comp_score > play_score and comp_score <= 21:
        print("You Lose!!")
    elif play_score > 21:
        print("You went over. You Lose!!")
    elif comp_score > 21:
        print("Opponent went over. You Win!!")
    elif comp_score == play_score and play_score > 21:
        print("You went over. You Lose!!")
    elif comp_score == play_score:
        print("Draw!!")


def game():
    print(logo)
    player_score = Add_player_card(0)
    computer_score = Add_computer_card(0)
    print(f"   Computer's first card: {computers_cards[0]}")
    flag = True
    while flag:
        card_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if card_choice == 'y':
            player_score = Add_player_card(player_score)
            print(f"   Computer's first card: {computers_cards[0]}")
            if player_score > 21:
                Final(computer_score,player_score)
                flag = False
            elif player_score == 21:
                Final(computer_score,player_score)
                flag = False
        elif card_choice == 'n':
            Final(computer_score,player_score)
            flag = False

while True:
    c = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if c == 'y':
        subprocess.run("cls", shell=True)
        players_cards = []
        player_score = 0
        computers_cards = []
        computer_score = 0
        game()
    elif c == 'n':
        break
    else:
        print("Invalid Option")