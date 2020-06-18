import django_filters
from django import forms
from .models import Post

class PostFilter(django_filters.FilterSet):
    impurity_name = django_filters.CharFilter(lookup_expr = 'icontains',label="Impurity Name")
    class Meta:
        model = Post
        fields = ['impurity_name']