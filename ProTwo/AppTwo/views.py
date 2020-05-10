from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Webpage,AccessRecord,Topic

def index(request):
    webpages = AccessRecord.objects.order_by('date')
    my_dict = {'access_records': webpages}
    return render(request,'first_app/index.html',context=my_dict)

def help(request):
    my_dict = {'help_person':'Vasudeva'}
    return render(request,"help_page/help.html",context=my_dict)

# Create your views here.   
