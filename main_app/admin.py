from django.contrib import admin

# Register your models here.

from .models import Photobook, Photo

admin.site.register(Photobook)
admin.site.register(Photo)