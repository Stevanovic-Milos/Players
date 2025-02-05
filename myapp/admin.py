from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)




admin.site.site_header = 'Admin'
admin.site.site_title = 'Admin'
admin.site.index_title= 'Uredi'
