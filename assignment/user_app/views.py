from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from user_app.models import User
from .signup import SignUp
from populate import populate

# Create your views here.


def index(request):
    return render(request, 'home.html')


def tables(request):
    users = User.objects.order_by('first_name')
    my_dict = {"users": users}
    return render(request, 'users/index.html', context=my_dict)


def form_page(request):
    form = SignUp(request.POST)
    form_dict = {'form': form}

    if request.method == "POST":
        if form.is_valid():
            print("here")
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            populate(1, first_name, last_name, email)
            users = User.objects.order_by('first_name')
            my_dict = {"users": users}
            return render(request, 'users/index.html', context=my_dict)
        else:
            print(form.errors)
    return render(request, 'form/signup_form.html', context=form_dict)
