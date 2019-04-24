from django.contrib import admin

# Register your models here.
from .models import Polls,Choice

admin.site.register(Polls)
admin.site.register(Choice)