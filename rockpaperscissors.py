#  a program to code a game which simulates rock, paper, scissors

import random

def play():
    user = input("What's your choice? 'r' for rock,'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    
    # r > s, p > r, s > p
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'


def is_win(player, opponent):
    # return true if player wins
    # r > s, p > r, s > p
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())