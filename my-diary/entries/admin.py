from django.contrib import admin

from .models import Entry #imports Entry from models.py
# Register your models here.

admin.site.register(Entry)  #registers Entry so we can see the Entry model in the django admin site