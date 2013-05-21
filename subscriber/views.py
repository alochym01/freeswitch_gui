from django.http import HttpResponse
from django.shortcuts import render_to_response
from subscriber.models import fsUser
from form_add import fsUserForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


# Create your views here.
def hello(request):
    name = "Alochym"
    html = "<html><body>Hi %s, This seems to have worked</body></html>" % name
    return HttpResponse(html)


def all(request):
    return render_to_response('base_subscriber.html',
                              {'fsUser': fsUser.objects.all()})


def add(request):
    if request.POST:
        form = fsUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/subscriber')
    else:
        form = fsUserForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('add_subscriber.html', args)
