from django.http import HttpResponse
def index(request):

    return HttpResponse("<h1>hello <h1>")


def about(request):
    return HttpResponse("hello world"
                        "")
