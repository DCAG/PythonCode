from __future__ import print_function

board = [['-', '-', '-'] for x in xrange(3)]

symbols = ['x', 'o']
playerTurn = symbols[0]

def PrintBoard():
    def PrintLine(row):
        print('#', end='')
        for item in row:
            print(item, end='')
        print('#')
    global board
    print('#'*5)
    for row in board:
        PrintLine(row)
    print('#'*5)

def getBoardItem(location):
    '''
    docstring: "hello" 
    '''
    global board
    return board[(location - location % 3) / 3][location % 3]

def isEmptyCell(location):
    '''
    docstring: "hello" 
    '''
    return getBoardItem(location) == '-'

def playMove():
    move = -1
    while True:
        move = raw_input("current player is ["+playerTurn+"] Enter a number(0-8):")
        try:
            move = int(move)
        except ValueError:
            print("not a number or not in range")
            continue
        if 0 > move or 8 < move:
            print('out of range')
            continue
        elif board[(move - move % 3) / 3][move % 3] != '-':
            print('This cell is already set')
            continue
        else:
            break
    board[(move - move % 3) / 3][move % 3] = playerTurn

def gameOver():
    global board
    sols = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 5, 8], [2, 4, 6], [3, 4, 5], [6, 7, 8]]
    for solution in sols:
        if getBoardItem(solution[0]) == getBoardItem(solution[1]) and getBoardItem(solution[1]) == getBoardItem(solution[2]):
            if getBoardItem(solution[0]) == 'x':
                print('x is the winner!')
                return True
            elif getBoardItem(solution[0]) == 'o':
                print('o is the winner')
                return True
            else:
                pass
    for i in range(0, 9):
        if isEmptyCell(i):
            break
    else:
        print('draw')
        return True
    return False

PrintBoard()
while not gameOver():
    playMove()
    if playerTurn == symbols[1]:
        playerTurn = symbols[0]
    else:
        playerTurn = symbols[1]
    PrintBoard()

PRESS_ANY_KEY = input_raw("press any key to continue")
'''
      2
  _ _ _ 
1 _ _ _
  6 7 8

5%3 = 2
5-2 = 3
3/3 = 1
'''