from django import forms
from loan_form.models import Property, Lender, Borrower, CoLender, Gurrantor
from .models import DocumentTemplate

class RecordForm(forms.Form):
    property = forms.ModelChoiceField(queryset=Property.objects.all(), label="Select Property", required=True)
    lender = forms.ModelChoiceField(queryset=Lender.objects.all(), label="Select Lender", required=True)
    borrower = forms.ModelChoiceField(queryset=Borrower.objects.all(), label="Select Borrower", required=True)
    colender = forms.ModelChoiceField(queryset=CoLender.objects.all(), label="Select Co-Lender", required=False)
    guarantor = forms.ModelChoiceField(queryset=Gurrantor.objects.all(), label="Select Gurrantor", required=False)
    document_template = forms.ModelMultipleChoiceField(
        queryset=DocumentTemplate.objects.all(),
        label="Select Document Template",
        required=True,
        widget=forms.CheckboxSelectMultiple,
        )