from django.contrib import admin

from .models import Post

# Register your models here.
admin.site.register(Post)           ### show table in the admin page so we can edit