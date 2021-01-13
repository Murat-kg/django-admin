from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Stadup




class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'group', 'user_name', 'done', 'todo', 'problems', 'publication')
    list_display_links = ('id', 'group', 'user_name', 'done', 'todo', 'problems', 'publication')
    list_filter = ['publication', 'group',]
    search_fields = ['user_name', ]


admin.site.register(Stadup, AuthorAdmin)
