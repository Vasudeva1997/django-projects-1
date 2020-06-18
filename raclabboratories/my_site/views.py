from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
from datetime import date
from .filters import PostFilter
from django.template import Context
from django.views.generic.edit import FormMixin


class PostListView(ListView):
    model = models.Post

    def get_context_data(self, *args, **kwargs):
        post_names = models.Post.objects.order_by('impurity_name')
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        names = {}
        for post_name in post_names:
            names[post_name.impurity_name] = post_name.id
        # myFilter = PostFilter(self.request.GET, queryset=post_names)
        # print(myFilter.request)
        # post_names = myFilter.qs
        if(len(post_names) > 6):
            post_names = post_names[0:6]
        context['names'] = names
        context['post_names'] = post_names
        # context['myFilter'] = myFilter
        return context

    template_name = "index.html"


class ProductsView(ListView):
    model = models.Post

    def get_context_data(self, *args, **kwargs):
        post_names = models.Post.objects.order_by('impurity_name')
        context = super(ProductsView, self).get_context_data(*args, **kwargs)
        names = {}
        for post_name in post_names:
            names[post_name.impurity_name] = post_name.id
        myFilter = PostFilter(self.request.GET, queryset=post_names)
        post_names = myFilter.qs
        context['names'] = names
        context['post_list'] = post_names
        context['myFilter'] = myFilter
        return context

    template_name = "my_site/products.html"


class PostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = "my_site/post_form.html"


class PostDetailView(DetailView):
    model = models.Post
    template_name = "my_site/post_details.html"


class OrderListView(LoginRequiredMixin, ListView):
    login_url = '/admin'
    model = models.Post
    template_name = "my_site/order_list.html"
    context_object_name = "posts"


def add_order(request, pk):
    posts = get_object_or_404(models.Post, pk=pk)
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
    return render(request, 'my_site/order_form.html', {'form': form, 'post': posts})
