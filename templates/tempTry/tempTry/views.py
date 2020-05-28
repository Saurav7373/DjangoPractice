from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params = {'name':'Saurav', 'place':'Ravi'}
    return render(request, 'index.html',params)
   #return HttpResponse("home")

def removepunc(request):

    return HttpResponse("Remove Punc")

def capfirst(request):
    return HttpResponse("Capitalized first")

def newlinerem(request):
    return HttpResponse("New Line Remover")
def spaceremover(request):
    return HttpResponse("Space Remover")
def charcount(request):
    return HttpResponse("Character Count")

