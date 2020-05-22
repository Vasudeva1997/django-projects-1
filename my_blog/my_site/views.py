from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView,)
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models
from . import forms
from django.urls import reverse_lazy

# Create your views here.

class IndexPage(TemplateView):
    template_name = "index.html"

class PostListView(ListView):
    model = models.Post
    template_name = "post_list.html"

class NewPost(LoginRequiredMixin,CreateView):
    login_url = "/accounts/login/"
    form_class = forms.NewPostForm
    model = models.Post
    template_name = "post_form.html"

class PostDetailView(LoginRequiredMixin,DetailView):
    login_url = "/accounts/login/"
    model = models.Post
    template_name = "post_details.html" 
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = "/accounts/login/"
    model = models.Post
    form_class = forms.NewPostForm
    template_name = "post_form.html"

class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = "/accounts/login/"
    model = models.Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy("my_site:post_list")

class DoLogout(LoginRequiredMixin,LogoutView):
    def get(self, request):
        return redirect("my_site:post_list")

class SignUpView(CreateView):
    form_class = forms.SignUpForm
    model = User
    template_name = 'signupForm.html'
    success_url = '/'

def add_comment(request,pk):
    post = get_object_or_404(models.Post,pk=pk)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('my_site:post_detail', pk=post.pk)
    else:
        form = forms.CommentForm()
    return render(request,'comment_form.html',{'form':form})

def remove_comment(request,pk):
    comment = get_object_or_404(models.Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('my_site:post_detail', pk=post_pk)