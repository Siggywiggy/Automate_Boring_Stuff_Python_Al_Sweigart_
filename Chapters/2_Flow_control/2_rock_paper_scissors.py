import random, sys
print('ROCK, PAPER, SCISSORS')

#tracking wins, losses and ties

wins = 0
losses = 0
ties = 0

while True: #main game loop
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True: #player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            print('Thanks for playing, exiting the game!')
            sys.exit() #quit the program
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break #break ou of the player input loop
        print('Type one of r, p, s or q.')

    #Display what the player chose:
    if player_move == 'r':
        print('ROCK vs ...')
    elif player_move == 'p':
        print('PAPER vs ...')
    elif player_move == 's':
        print('SCISORS vs ...')
    
    #Display computers choice:
    random_number = random.randint(1,3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS')
    
    #display and record the win/loss/tie
    if player_move == computer_move:
        print('Its a tie!')
        ties += 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins += 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins += 1
    else:
        print('You loose!')
        losses += 1