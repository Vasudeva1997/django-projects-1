from django.contrib import admin
from .models import Post,PostDetails

# Register your models here.

admin.site.register(Post)
admin.site.register(PostDetails)