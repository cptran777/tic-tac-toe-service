from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from modules.play import make_play, check_victory
import json

def index(request):

  if (request.method == 'GET'): 
    return JsonResponse({'message': 'This is a service for tic tac toe'})
  else:
    return JsonResponse({'message': 'Please only make a GET request'})

# Play expects a request to have a body with a data array that represents the positions of the board
def play(request):

  query_data = dict(request.GET.iterlists())

  # Recreate the board from the query:
  board = []

  for x in range(3):
    board.append(query_data['data[%d][]' % (x)])

  print(board)

  if check_victory(board, '1'):
    print('victory detected')
    return JsonResponse({
      'board': board,
      'victory': 1
    })

  newBoard = make_play(board)

  print(newBoard)

  if check_victory(newBoard, '2'):
    return JsonResponse({
      'board': newBoard,
      'victory': 2
    })
  else: 
    return JsonResponse({
      'board': newBoard,
      'victory': 0
    })


