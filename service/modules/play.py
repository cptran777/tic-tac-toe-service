from django.core import serializers
from random import randint

# Takes a board and a number and checks the board for potential vertical matches of that number
def check_vert(board, num):

  for col in range(len(board)):
    vert_count = 0
    for row in range(len(board)):
      if (board[row][col] == num):
        vert_count += 1




def make_play(board):

  print('here is the board: ')
  print(board)

  empty = []

  for row in range(len(board)):
    for col in range(len(board)):
      if (board[row][col] == '0'):
        empty.append([row, col])

  pick = empty[randint(0, len(empty) - 1)]

  board[pick[0]][pick[1]] = '2'

  return board

def check_diagonal_left(board, player):

  print('inside check_diagonal_left')

  for x in range(3):
    print(board[x][x])
    print(player)
    if board[x][x] != player:
      return False

  return True

def check_diagonal_right(board, player):

  x = 0
  y = 2

  while x < 3:
    if board[x][y] != player:
      return False
    x += 1
    y -= 1

  return True

def check_row(row, player):

  for item in row: 
    if item != player:
      return False

  return True

def check_column(board, col, player):

  for row in board:
    if (row[col] != player):
      return False

  return True

def check_victory(board, player):

  for row in board:
    if check_row(row, player):
      return True

  for x in range(3):
    if check_column(board, x, player):
      return True

  if check_diagonal_left(board, player):
    return True

  if check_diagonal_right(board, player): 
    return True

  return False


