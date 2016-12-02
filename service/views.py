from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

# Create your views here.
def index(request):

  if (request.method == 'GET'): 
    return JsonResponse({'message': 'This is a service for tic tac toe'})
  else:
    return JsonResponse({'message': 'Please only make a GET request'})

def play(request):

  print request.body
  return JsonResponse({'message': 'Response'})
