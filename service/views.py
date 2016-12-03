from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

def index(request):

  if (request.method == 'GET'): 
    return JsonResponse({'message': 'This is a service for tic tac toe'})
  else:
    return JsonResponse({'message': 'Please only make a GET request'})

# Play expects a request to have a body with a data array that represents the positions of the board
def play(request):

  if (hasattr(request.body, 'data')):
    print(request.body.data)

  else:
    print('no data')
    return JsonResponse({'message': 'Response'})
