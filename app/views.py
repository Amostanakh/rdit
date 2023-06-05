from pdb import post_mortem
from django.shortcuts import redirect, render
from app.forms import CrudForm, RegForm, UpdateForm, UserForm
from django.contrib.auth import logout
from .models import User


# Create your views here.
def users(request):
    context = {'form': UserForm()}
    return render(request, 'login.html', context)



def signup(request):
        context = {'register': RegForm()}
        return render(request, 'register.html', context)

 
def signout(request):
    logout(request)
    return redirect('login/')


def admin(request):
     user = {'admin': CrudForm()}
     return render( request, 'admin.html', user)


def addy(request):
    addUser = {'myUpdate':  CrudForm()}
    return render(request,'add.html', addUser)

def delete(id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect("/")

def update(request):
     upUser = {'myUpdate': UpdateForm()}
     return render(request,'update.html', upUser)









