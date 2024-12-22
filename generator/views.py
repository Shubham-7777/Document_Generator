from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .forms import RecordForm
from .models import DocumentTemplate
from docxtpl import DocxTemplate
import jinja2
import tempfile
from django.template import loader
import zipfile

def main_menu(request):
    template = loader.get_template('main_menu.html')
    return HttpResponse(template.render())

def multiply_by(value, by):
    return value * by


from django.shortcuts import render
from django.http import FileResponse
import zipfile
import tempfile
from docxtpl import DocxTemplate
import jinja2


def process_form(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)

        if form.is_valid():
            # Extract cleaned data from the form
            document_templates = form.cleaned_data['document_template']
            property_instance = form.cleaned_data['property']
            lender_instance = form.cleaned_data['lender']
            borrower_instance = form.cleaned_data['borrower']
            colender_instance = form.cleaned_data['colender']
            guarantor_instance = form.cleaned_data['guarantor']

            # Create a shared context dictionary with all extracted data
            jinja_env = jinja2.Environment()
            jinja_env.filters['multiply_by'] = multiply_by  # Custom filters applied to Jinja2 environment

            context = {
                'property': {
                    'loan_number': property_instance.loan_number,
                    'street_address': property_instance.street_address,
                    'city': property_instance.city,
                    'state': property_instance.state,
                    'zip': property_instance.zip,
                    'interest_rate': property_instance.interest_rate,
                    'loan_amount': property_instance.loan_amount,
                    'text_representation': property_instance.text_representation,
                    'rehab_withhold': property_instance.rehab_withhold,
                    'funding_date': property_instance.funding_date,
                    'maturity_date': property_instance.maturity_date,
                    'monthly_payment': property_instance.monthly_payment,
                    'default_rate': property_instance.default_rate,
                },
                'lender': {
                    'name': lender_instance.name,
                    'street_address1': lender_instance.street_address1,
                    'street_address2': lender_instance.street_address2,
                    'city': lender_instance.city,
                    'state': lender_instance.state,
                    'zip': lender_instance.zip,
                    'email': lender_instance.email,
                    'phone': lender_instance.phone,
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
                    'phone': colender_instance.phone,
                },
                'guarantor': {
                    'name': guarantor_instance.name,
                    'street_address1': guarantor_instance.street_address1,
                    'city': guarantor_instance.city,
                    'state': guarantor_instance.state,
                    'zip': guarantor_instance.zip,
                    'email': guarantor_instance.email,
                    'phone': guarantor_instance.phone,
                },
            }

            # Create a temporary ZIP file to save multiple generated documents
            with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as zip_tmp:
                with zipfile.ZipFile(zip_tmp, 'w') as zipf:
                    # Loop through all selected templates
                    for template in document_templates:
                        try:
                            # Generate path for each document template
                            template_file_path = template.template_file.path
                            doc = DocxTemplate(template_file_path)

                            # Render the context into each document template
                            doc.render(context, jinja_env)

                            # Save rendered document to a temporary file
                            with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_file:
                                tmp_file_path = tmp_file.name
                                doc.save(tmp_file_path)

                                # Add the rendered file to the ZIP archive
                                zipf.write(tmp_file_path, arcname=f"{template.name}_filled.docx")
                        except Exception as e:
                            print(f"Error processing template {template.name}: {e}")

            # Return ZIP file as response
            zip_tmp_path = zip_tmp.name
            response = FileResponse(open(zip_tmp_path, 'rb'), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="generated_documents.zip"'
            return response

    # Handle GET request or invalid form submissions
    else:
        form = RecordForm()

    # Render the form if it's a GET request or the form isn't valid
    return render(request, 'docs_form.html', {'form': form})



"""
def process_form(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            document_templates = form.cleaned_data['document_template']
            #template_file_path = document_template.template_file.path
            for template in document_templates:
            # Access template_file.path for each selected template
                template_file_path = template.template_file.path
                print(template_file_path, "template_file_path")
                #print(template_file_path)

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
            response['Content-Disposition'] = f'attachment; filename="{document_templates.name}_filled.docx"'

            return response  # Directly return the response

    else:
        form = RecordForm()

    return render(request, 'docs_form.html', {'form': form})
"""