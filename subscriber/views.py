from django.shortcuts import render_to_response
from subscriber.models import fsUser
from form_add import fsUserForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


# Create your views here.
def all(request):
    return render_to_response('fsUsers.html',
                              {'fsUsers': fsUser.objects.all()})


def getUser(request, user_id=1):
    return render_to_response('fsUser.html',
                              {'fsUser': fsUser.objects.get(id=user_id)})


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
    return render_to_response('form_add_subscriber.html', args)


def edit(request, user_id):
    fsUser_id = fsUser.objects.get(id=user_id)
    form = fsUserForm(instance=fsUser_id)
    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['id'] = user_id
    return render_to_response('form_update_subscriber.html', args)


def update(request):
    if request.POST:
        form = fsUserForm(request.POST)
        user_id = request.POST['User_id']
        fsUser_id = fsUser.objects.get(id=user_id)
        if form.is_valid():
        #    fsUser_id = fsUser.objects.get(id=request.POST['User_id'])
#            print type(fsUser_id)
            fsUser_id.Username = form['Username'].value()
            fsUser_id.Password = form['Password'].value()
            fsUser_id.Toll_allow = form['Toll_allow'].value()
            fsUser_id.User_context = form['User_context'].value()
            fsUser_id.save()
            return HttpResponseRedirect('/subscriber')
        else:
            fsUser_id = fsUser.objects.get(id=user_id)
            form = fsUserForm(instance=fsUser_id)
            args = {}
            args.update(csrf(request))
            args['form'] = form
            args['id'] = user_id
            return render_to_response('form_update_subscriber.html', args)
