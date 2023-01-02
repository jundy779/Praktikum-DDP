from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  context = {
    "name": "Jundi"
  }
  return render(request, 'index.html', context=context)
