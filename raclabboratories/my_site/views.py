from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,CreateView,DetailView
from . import models
from . import forms
from datetime import date
# Create your views here.

class PostListView(ListView):
    model = models.Post
    template_name = "my_site/post_list.html"


class PostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = "my_site/post_form.html"

class PostDetailView(DetailView):
    model = models.Post
    template_name = "my_site/post_details.html"
    
class OrderListView(ListView):
    model = models.Post
    template_name = "my_site/order_list.html"
    context_object_name = "posts"
    

def add_order(request,pk):
    posts = get_object_or_404(models.Post,pk=pk)
    if request.method == "POST":
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.post = posts
            order.datetime = date.today()
            order.save()
            return redirect('my_site:post_list')
    else:
        form = forms.OrderForm()
    return render(request,'my_site/order_form.html',{'form':form,'post':posts})
