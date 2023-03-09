from django.contrib import admin
from .models import *
# Register your models here.

class CsvFileAdmin(admin.ModelAdmin):
    pass
admin.site.register(CsvFile,CsvFileAdmin)


class FileDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(FileDetails,FileDetailsAdmin)


