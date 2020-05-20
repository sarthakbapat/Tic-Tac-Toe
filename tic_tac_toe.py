from IPython.display import clear_output
import random

def display_board(board):
   # num_pad = [0,7,8,9,4,5,6,1,2,3]
    print(' {} | {} | {} '.format(board[1],board[2],board[3]))
    print('-----------')
    print(' {} | {} | {} '.format(board[4],board[5],board[6]))
    print('-----------')
    print(' {} | {} | {} '.format(board[7],board[8],board[9]))


def player_input():
    print('Player 1 gets a chance to select marker')
    print('Marker can be X or O')
    marker = []
    while(1):
        marker_player1 = input('Please select your marker')
        if marker_player1 == 'X' or marker_player1 == 'O':
            break
        else:
            print('Error! Marker can be X or O')
    
    #Set marker for player 2 default by checking player 1 marker.
    if marker_player1 == 'X':
        marker_player2 = 'O'
    else:
        marker_player2 = 'X'
    #Store the markers in the list.    
    marker = [marker_player1,marker_player2]
    return marker

def place_marker(board, marker, position):
    if position not in range(1,10):
        print('Invalid Position\n')
    else:
        board[position] = marker


def win_check(board, mark):
    l1 = [7,4,1]
    l2 = [7,8,9]
    if board[7]==mark and board[5]==mark and board[3]==mark:
        return True
    if board[1]==mark and board[5]==mark and board[9]==mark:
        return True
    for item in l1:
        if board[item]==mark and board[item+1]==mark and board[item+2]==mark:
            return True
    for item in l2:
        if board[item]==mark and board[item-3]==mark and board[item-6]==mark:
            return True


def choose_first():
    select = random.randint(1,2)
    #go_first = 'Player ' + select + ' goes first'
    return select

def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True


def full_board_check(board):
    count_full = 0
    for item in board:
        if item == 'X' or item == 'O':
            count_full+=1
    
    return (count_full == 9)


def player_choice(board):
    while(1):
        position = int(input('Please enter the next position\n'))
        if position not in range(1,10):
            print('Incorrect position - Only 1-9 allowed\n')
        else:
            break
            
    if space_check(board,position):
        return position


def replay():
    play_again = input('Do you want to play again ? Y or N\n')
    return play_again == 'Y'

print('Welcome to Tic Tac Toe!')

while(1):
    board = ['$',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    display_board(board)
    
    marker = player_input()
    player_1_mark = marker[0]
    player_2_mark = marker[1]
    
    first_to_play = choose_first()
    if first_to_play == 1:
        second = 2
    else:
        second = 1
    print('Player '+ str(first_to_play) + ' to go first!\n')
    
    while(1):
        if first_to_play == 1:
            mark = player_1_mark
        else:
            mark = player_2_mark
            
        position = player_choice(board)
        place_marker(board,mark,position)
        display_board(board)
         
        if win_check(board,mark):
            print('Player ' + str(first_to_play) + ' has won !\n')
            break
        elif full_board_check(board):
            print('Board full - Game Drawn !\n')
            break
        else:
            pass
        
        
        if mark == player_1_mark:
            mark = player_2_mark
        else:
            mark = player_1_mark
            
        position = player_choice(board)
        place_marker(board,mark,position)
        display_board(board)
        
        if win_check(board,mark):
            print('Player ' + str(second) + ' has won !\n')
            break
        elif full_board_check(board):
            print('Board full - Game Drawn !\n')
            break
        else:
            pass
        
    
    if not replay():
        break
        