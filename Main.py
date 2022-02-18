from random import randrange
from os import system
board = [['1','2','3'],['4','X','6'],['7','8','9']]

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[0][0] + "   |   " + board[0][1] + "   |   " + board[0][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[1][0] + "   |   " + board[1][1] + "   |   " + board[1][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[2][0] + "   |   " + board[2][1] + "   |   " + board[2][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 'X' or board[row][column] == 'O':
                continue
            else:
                free_fields.append((row, column))
    return free_fields


def move_tuple(move):
    if move == 1:
        co = (0, 0)
    elif move == 2:
        co = (0,1)
    elif move == 3:
        co = (0,2)
    elif move == 4:
        co = (1,0)
    elif move == 5:
        co = (1,1)
    elif move == 6:
        co = (1,2)
    elif move == 7:
        co = (2,0)
    elif move == 8:
        co = (2,1)
    elif move == 9:
        co = (2,2)
    return co

def enter_move(board):
    
    while True :
        move = int(input("Enter your move: "))
        if move > 9 or move < 1:
            break
        co = move_tuple(move)
        free = make_list_of_free_fields(board)
        if co in free:
            board[co[0]][co[1]] = 'O'
            break
        else:
            print("Invalid move")



def draw_move(board):
    while True :
        co = move_tuple(randrange(9)+1)
        free = make_list_of_free_fields(board)
        if co in free:
            board[co[0]][co[1]] = 'X'
            break
 
  
def victory_for(board, sign):
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True
    for column in range(len(board)):
        if board[0][column] == board[1][column] == board[2][column] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
            return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
            return True
    return False

Winner = False
display_board(board)
while not Winner:

    enter_move(board)
    display_board(board)

    
    if victory_for(board, 'O'):
        print("Buena mostrico!")
        Winner = True
        break
    system("cls")
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("La maquina te ha ganado, mucha bestia!")
        Winner = True
   
    elif len(make_list_of_free_fields(board)) == 0:
        print("Empate!")
        Winner = True

