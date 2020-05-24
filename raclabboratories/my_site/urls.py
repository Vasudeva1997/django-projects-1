from django.urls import path
from . import views

app_name='my_site'

urlpatterns = [
    path('',views.PostListView.as_view(),name="post_list"),
    path('new_post/',views.PostCreateView.as_view(),name="new_post"),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name="post_details"),
    path('order/',views.OrderListView.as_view(),name="order_details"),
    path('post/<int:pk>/add_order',views.add_order,name="add_order"),
]