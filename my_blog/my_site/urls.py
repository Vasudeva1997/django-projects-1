from django.contrib import admin
from django.urls import path
from . import views

app_name = 'my_site'
urlpatterns = [
    path('', views.IndexPage.as_view(), name="index"),
    path('posts/',views.PostListView.as_view(),name="post_list"),
    path('newpost/', views.NewPost.as_view(), name="new_post"),
    path("posts/<int:pk>/",views.PostDetailView.as_view(),name="post_detail"),
    path("posts/<int:pk>/update/",views.PostUpdateView.as_view(),name="update_detail"),
    path("posts/<int:pk>/delete/",views.PostDeleteView.as_view(),name="delete_detail"),
    path("posts/<int:pk>/comment",views.add_comment,name="add_comment"),
    path("comment/<int:pk>/delete",views.remove_comment,name="delete_comment"),
]
