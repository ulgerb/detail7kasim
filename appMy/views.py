from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
   cards = Card.objects.all()
   context={
      "cards":cards,
   }
   return render(request, 'index.html',context)


def Detail(request):
   context = {}
   return render(request, 'detail.html')
