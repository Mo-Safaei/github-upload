from django.contrib import admin

# Register your models here.

from .models import Singer, Song

admin.site.register(Singer)
admin.site.register(Song)




