from django.contrib import admin
from .models import Lender, Borrower, DocumentTemplate, ExcelUpload

class LenderAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DocumentTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_file')

class ExcelUploadAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')

admin.site.register(Lender, LenderAdmin)
admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(DocumentTemplate, DocumentTemplateAdmin)
admin.site.register(ExcelUpload, ExcelUploadAdmin)
