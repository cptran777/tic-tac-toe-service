from django.core import serializers
from random import randint

import json

# Takes a board and a number and checks the board for potential vertical matches of that number
def check_vert(board, num):

  for col in range(len(board)):
    vert_count = 0
    for row in range(len(board)):
      if (board[row][col] == num):
        vert_count += 1
        if (vert_count > 1):




def make_play(board):

  empty = []

  for row in range(len(board)):
    for col in range(len(board)):
      if (board[row][col] == 0):
        empty.append([row, col])

  pick = empty[randint(0, len(empty) - 1)]

  board[pick[0]][pick[1]] = 2

  return board
