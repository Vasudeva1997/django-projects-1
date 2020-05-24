from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView
from . import models
from . import forms

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

class OrderCreateView(CreateView):
    model = models.Post
    form_class = forms.OrderForm
    template_name = "my_site/order_form.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = models.Post.objects.filter(id=self.kwargs['pk'])
        return context