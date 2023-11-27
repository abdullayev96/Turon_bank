from django.contrib import admin
from .models import *


class AdminFile(admin.ModelAdmin):
     list_display = ['id', 'file_name', 'file_type', 'size', 'created_at']

     list_filter = ['id', 'created_at']


admin.site.register(File, AdminFile)

