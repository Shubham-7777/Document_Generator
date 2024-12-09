from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .forms import RecordForm
from .models import DocumentTemplate
from docxtpl import DocxTemplate
import jinja2
import tempfile
from django.template import loader

def main_menu(request):
    template = loader.get_template('main_menu.html')
    return HttpResponse(template.render())

def multiply_by(value, by):
    return value * by

def process_form(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            document_template = form.cleaned_data['document_template']
            template_file_path = document_template.template_file.path
            print(template_file_path)

            property_instance = form.cleaned_data['property']
            lender_instance = form.cleaned_data['lender']
            borrower_instance = form.cleaned_data['borrower']
            colender_instance = form.cleaned_data['colender']
            guarantor_instance = form.cleaned_data['guarantor']

            doc = DocxTemplate(template_file_path)

            jinja_env = jinja2.Environment()
            jinja_env.filters['multiply_by'] = multiply_by

            context = {
                'property': {
                    'loan_number': property_instance.loan_number,
                    'street_address': property_instance.street_address,
                    'city': property_instance.city,
                    'state': property_instance.state,
                    'zip': property_instance.zip,
                    'interest_rate': property_instance.interest_rate,
                    'loan_amount': property_instance.loan_amount,
                    'rehab_withhold': property_instance.rehab_withhold,
                    'funding_date': property_instance.funding_date,
                    'maturity_date': property_instance.maturity_date,
                    'monthly_payment': property_instance.monthly_payment,
                    'default_rate': property_instance.default_rate
                },
                'lender': {
                    'name': lender_instance.name,
                    'street_address1': lender_instance.street_address1,
                    'street_address2': lender_instance.street_address2,
                    'city': lender_instance.city,
                    'state': lender_instance.state,
                    'zip': lender_instance.zip,
                    'email': lender_instance.email,
                    'phone': lender_instance.phone
                },
                'borrower': {
                    'name': borrower_instance.name,
                    'street_address1': borrower_instance.street_address1,
                    'city': borrower_instance.city,
                    'state': borrower_instance.state,
                    'zip': borrower_instance.zip,
                    'email': borrower_instance.email,
                    'phone': borrower_instance.phone,
                    'signer': borrower_instance.signer,
                    'title': borrower_instance.title,
                },
                'colender': {
                    'name': colender_instance.name,
                    'street_address1': colender_instance.street_address1,
                    'city': colender_instance.city,
                    'state': colender_instance.state,
                    'zip': colender_instance.zip,
                    'email': colender_instance.email,
                    'phone': colender_instance.phone
                },
                'guarantor': {
                    'name': guarantor_instance.name,
                    'street_address1': guarantor_instance.street_address1,
                    'city': guarantor_instance.city,
                    'state': guarantor_instance.state,
                    'zip': guarantor_instance.zip,
                    'email': guarantor_instance.email,
                    'phone': guarantor_instance.phone
                },
            }

            doc.render(context, jinja_env)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_file:
                tmp_file_path = tmp_file.name
                doc.save(tmp_file_path)

            # Return the file as a response, no redirect needed
            response = FileResponse(open(tmp_file_path, 'rb'), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename="{document_template.name}_filled.docx"'

            return response  # Directly return the response

    else:
        form = RecordForm()

    return render(request, 'docs_form.html', {'form': form})
