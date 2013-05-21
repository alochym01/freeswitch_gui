from django.shortcuts import render_to_response
from django.http import HttpResponse


def home01(request):
    name = "Alochym"
    html = "<html><body>Hi %s, This seems to have worked</body></html>" % name
    return HttpResponse(html)


def home(request):
        return render_to_response('home.html')
