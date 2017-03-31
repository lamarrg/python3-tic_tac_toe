import matplotlib.pyplot as plt
import numpy as np
import random
import time 

def create_board():
    return np.zeros((3,3))

def place(board, player, position):
    if board[position[0], position[1]] == 0:
        board[position[0], position[1]] = player

final_array = []

def possibilities(board):
    t = np.where(board == 0)
    q = np.column_stack((t[0], t[1]))
    for x in q:
        final_array.append((x[0], x[1]))
    return final_array

def random_place(board, player):
    random_placement = random.choice(possibilities(board))
    place(board, player, random_placement)


def col_win(board, player):
    for x in range(3):
        if all(item == player for item in board[x, :]):
            return True
        return False


def row_win(board, player):
    for x in range(3):
        if all(item == player for item in board[:,x]):
            return True
        return False


def diag_win(board, player):
    diag_one = [board[0,0], board[1,1], board[2,2]]
    diag_two = [board[0,2], board[1,1], board[2,0]]
    if (all(item == player for item in diag_one) or all(item == player for item in diag_two)):
        return True
    else:
        return False


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
            return winner
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
    
def play_strategic_game():
	board = create_board()
	winner = 0
	board[1,1] = 1 # defaults to having player 1 start in the center
	while winner == 0:
		for player in [2,1]:
			random_place(board, player)
			winner = evaluate(board)
			if winner != 0:
				break
	return winner


board = create_board()
print(board)
# print(time.clock())
print(play_strategic_game())


place(board, 1, (0,0)) # per instructions, places a "1" in position 0,0
place(board, 1, (1,1))
place(board, 1, (2,2))


# possibilities(board)
#
# print(random.choice(possibilities(board)))
#
#
# random_place(board, 2)

diag_win(board, 1)