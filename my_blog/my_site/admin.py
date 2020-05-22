from django.contrib import admin
from .models import Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields=("title","description","image_url")

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)