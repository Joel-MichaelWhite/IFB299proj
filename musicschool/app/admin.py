from django.contrib import admin
from .models import Students, Admins, Teachers

admin.site.register(Students)
admin.site.register(Admins)
admin.site.register(Teachers)
