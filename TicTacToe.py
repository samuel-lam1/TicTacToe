'''Tic Tac Toe game'''
from IPython.display import clear_output

def display(fie):
    ''' Display the game'''
    clear_output()
    for count in range(0,3):
        print('{}|{}|{}    position numbers:  {}|{}|{}\n'.
              format(fie[count][0],fie[count][1],fie[count][2],
                    count*3+1,count*3+2,count*3+3))

def player_choice(play, ava):
    '''Collect user position choice'''
    cho = 'x'
    while cho.isdigit() is False or int(cho) not in available:
        cho = input(f"Player {play}'s turn. Please input your choice (1~9): ")
        if cho.isdigit() is False or int(cho) not in range(1,10):
            print('Sorry, input is not valid.\n')
        elif int(cho) not in ava:
            print('Position has been taken, please choose another.\n')
    return int(cho)

def player_mark(fie,position,mar):
    '''Change user's chosen position into their mark'''
    if position <= 3:
        fie[0][position-1] = mar
    elif position >= 7:
        fie[2][position-7] = mar
    else:
        fie[1][position-4] = mar

def check_win(fie):
    '''Check if any win condition is met'''
    for n in range(0,3):
        if ((len(set(fie[n]))==1 and set(fie[n]) != {'-'}) or
           (fie[0][n] == fie[1][n] == fie[2][n] and fie[0][n] != '-')):
            return True
    if ((fie[0][0] == fie[1][1] == fie[2][2] or
       fie[0][2] == fie[1][1] == fie[2][0]) and
       fie[1][1] != '-'):
        return True
    return False

def statement(win):
    '''Display the corresponding statement for win or draw game'''
    if win:
        print(f'Congratulations! Player {player} win!')
    else:
        print("It's a draw game!")

def again():
    '''Ask player if they want to play again'''
    game ='x'
    while game not in ['Y','y','N','n']:
        game = input('Do you want to play again? (Y/N) ')
        if game not in ['Y','y','N','n']:
            print('Sorry, but your input is not valid.')
    return game

while True:
    field = [['-','-','-'],['-','-','-'],['-','-','-']]
    player = 2
    mark = ['X', 'O']
    draw = False
    available = list(range(1,10))
    while check_win(field) is False and draw is False:
        player = player%2+1
        display(field)
        choice = player_choice(player, available)
        player_mark(field, choice, mark[player-1])
        available.remove(choice)
        draw = available == []
        display(field)
    statement(check_win(field))
    if again() in ['N','n']:
        break
