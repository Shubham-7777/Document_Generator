from django.contrib import admin
from .models import DocumentTemplate


class DocumentTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_file')

admin.site.register(DocumentTemplate, DocumentTemplateAdmin)