from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from django.forms.utils import ErrorDict
# django.forms.utils.ErrorDict
# Create your views here.

def index(request):
    return HttpResponse("<em>Passed HTML COde </em>")


def form_name_view(request):
    form = forms.FormName(request.POST)
    form_dict = {'form':form}
    if request.method == "POST":
        if form.is_valid():
            print(form)
            print("VALIDATION SUCCESS")
            print("NAME \t : \t"+form.cleaned_data['name'])
            print("EMAIL \t : \t"+form.cleaned_data['email'])
            print("TEXT \t : \t"+form.cleaned_data['text'])
        else:
            form_dict['errorMessage'] = ErrorDict(form.errors).get_json_data().get('__all__')[0]['message']
            return render(request,'form/form_page.html',context=form_dict)
    return render(request,'form/form_page.html',context=form_dict)