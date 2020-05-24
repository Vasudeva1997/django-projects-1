from django.contrib import admin
from .models import Post,PostDetails,Order

# Register your models here.

admin.site.register(Post)
admin.site.register(PostDetails)
admin.site.register(Order)
