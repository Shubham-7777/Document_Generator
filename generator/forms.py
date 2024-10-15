from django import forms
from .models import Lender, Borrower, DocumentTemplate, ExcelUpload
from .models import DocumentTemplate

class DocumentGenerationForm(forms.Form):
    excel_file = forms.FileField(label='Upload Excel File')
    lender = forms.ModelChoiceField(queryset=Lender.objects.all(), label='Lender')
    borrower = forms.ModelChoiceField(queryset=Borrower.objects.all(), label='Borrower')
    documents = forms.ModelMultipleChoiceField(queryset=DocumentTemplate.objects.all(), widget=forms.CheckboxSelectMultiple)


class DocumentTemplateForm(forms.ModelForm):
    class Meta:
        model = DocumentTemplate
        fields = ['name', 'template_file']


class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Upload Excel File')
