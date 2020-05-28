from django.http import HttpResponse
def index(request):

   return HttpResponse("home")

def removepunc(request):

    return HttpResponse("Remove Punc")
a
def capfirst(request):
    return HttpResponse("Capitalized first")

def newlinerem(request):
    return HttpResponse("New Line Remover")
def spaceremover(request):
    return HttpResponse("Space Remover")
def charcount(request):
    return HttpResponse("Character Count")

