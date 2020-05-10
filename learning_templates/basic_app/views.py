from django.shortcuts import render
from .forms import UserForm, UserProfileInfo
from django.forms.utils import ErrorDict
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    user_form = UserForm()
    user_profile = UserProfileInfo()
    my_dict = {'user_form': user_form, 'user_profile': user_profile}

    return render(request, 'basic_app/index.html', context=my_dict)


def register(request):
    registered = False
    my_dict= {}
    user_error_message = None
    form_error_message = None
    if request.method == "POST":
        user_form = UserForm(request.POST)
        user_profile = UserProfileInfo(request.POST)

        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            # print(type(user_form.errors.as_json()))
            if user_form.errors:
                user_error = ErrorDict(user_form.errors).get_json_data()
                for key in user_error:
                    user_error_message = user_error[key][0]["message"]
                    print(key,user_error[key][0]["message"])
            if user_profile.errors:
                form_error = ErrorDict(user_profile.errors).get_json_data()
                for key in form_error:
                    form_error_message = user_profile[key][0]["message"]
                    print(key,user_profile[key][0]["message"])
                
        my_dict = {
            'user_form': user_form, 'user_profile': user_profile,'registered': registered,
            'user_error' : user_error_message, 'form_error' : form_error_message
            }
    else:
        user_form = UserForm()
        profile_form = UserProfileInfo()
        my_dict = {'user_form': user_form, 'user_profile': profile_form,'registered': registered}    
    return render(request, 'basic_app/register.html', context=my_dict)


def other(request):
    return render(request, 'basic_app/other.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)
        print(user)
        if user:
            print("user authenticated")            
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponseRedirect("Accoutn not active")
        else:
            print("LOGIN FAILED")
            return HttpResponse("Invadiled Login")
    else:
        return render(request, 'basic_app/login.html')

@login_required  
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def relative(request):
    return render(request, 'basic_app/relative_url_template.html')
