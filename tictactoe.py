from __future__ import print_function

BOARD = [['-', '-', '-'] for x in xrange(3)]

SYMBOLS = ['x', 'o']
PLAYER_TURN = SYMBOLS[0]

def print_board():
    '''
    docstring: print_board
    '''
    def print_line(row):
        '''
        docstring: print_line
        '''
        print('#', end='')
        for item in row:
            print(item, end='')
        print('#')
    global BOARD
    print('#'*5)
    for row in BOARD:
        print_line(row)
    print('#'*5)

def get_board_item(location):
    '''
    docstring: get_board_item
    '''
    global BOARD
    return BOARD[(location - location % 3) / 3][location % 3]

def is_empty_cell(location):
    '''
    docstring: is_empty_cell
    '''
    return get_board_item(location) == '-'

def play_move():
    '''
    docstring: play_move
    '''
    move = -1
    while True:
        move = raw_input("current player is [%s] Enter a number(0-8):"%PLAYER_TURN)
        try:
            move = int(move)
        except ValueError:
            print("not a number or not in range")
            continue
        if move < 0 or move > 8:
            print('out of range')
            continue
        elif get_board_item(move) != '-':
            print('This cell is already set')
            continue
        else:
            break
    BOARD[(move - move % 3) / 3][move % 3] = PLAYER_TURN

def game_over():
    '''
    docstring: game_over
    '''
    global BOARD
    sols = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 5, 8], [2, 4, 6], [3, 4, 5], [6, 7, 8]]
    for solution in sols:
        if get_board_item(solution[0]) == get_board_item(solution[1]) and get_board_item(solution[1]) == get_board_item(solution[2]) and get_board_item(solution[0]) in SYMBOLS:
            print('%s is the winner!'%get_board_item(solution[0]))
            return True
    for i in range(0, 9):
        if is_empty_cell(i):
            break
    else:
        print('draw')
        return True
    return False

print_board()
while not game_over():
    play_move()
    if PLAYER_TURN == SYMBOLS[1]:
        PLAYER_TURN = SYMBOLS[0]
    else:
        PLAYER_TURN = SYMBOLS[1]
    print_board()

PRESS_ANY_KEY = raw_input("press any key to continue")
