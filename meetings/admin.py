from django.contrib import admin
from .models import Room
from .models import Meeting

admin.site.register(Meeting)
admin.site.register(Room)
