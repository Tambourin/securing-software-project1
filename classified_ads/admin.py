from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Ad, PoorUser

admin.site.register(Ad)
admin.site.register(PoorUser)