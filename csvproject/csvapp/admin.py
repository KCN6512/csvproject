from django.contrib import admin

from .models import *

# Register your models here.
class CsvModelAdmin(admin.ModelAdmin):
    list_display = ('file',)
    search_fields = ('file',)#нужно передать кортеж поэтому запятая,


admin.site.register(FileUploadModel,CsvModelAdmin)