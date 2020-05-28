from django.shortcuts import HttpResponse

def navigation(request):
    s = '''<h2>Navigation Bar<br></h2>
            <a href="https://github.com/Saurav7373/Map-of-nepal"Map-of nepal</a><br> 
            <a href="https://www.facebook.com/">Facebook</a><br>
            <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)

