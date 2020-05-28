from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
   #return HttpResponse("home")

def removepunc(request):
    #get the text
    djtext= (request.GET.get('text','default'))
    print(djtext)
    #analyze the text

    return HttpResponse("Remove Punc")

def capfirst(request):
    return HttpResponse("Capitalized first")

def newlinerem(request):
    return HttpResponse("New Line Remover")
def spaceremover(request):
    return HttpResponse("Space Remover")
def charcount(request):
    return HttpResponse("Character Count")

