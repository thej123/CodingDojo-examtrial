from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'semiRestfulUsers/index.html', {'users': User.objects.all() })

def new(request):
    return render(request, 'semiRestfulUsers/new.html')

def show(request, id):
    # print id
    user=User.objects.get(id=id)
    return render(request, 'semiRestfulUsers/show.html', {'user': user} )

def edit(request, id):
    user=User.objects.get(id=id)
    return render(request, 'semiRestfulUsers/edit.html', {'user': user} )

def delete(request, id):
    User.objects.get(id=id).delete()
    return redirect('/')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/users/new')
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email = request.POST['email'])
        return redirect('/users')

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/users/'+id+'/edit')
    else:
        user = User.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/')

