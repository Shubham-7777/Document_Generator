from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Property, CoLender, Lender, Borrower, Gurrantor
from num2words import num2words


def borrower(request):
    template = loader.get_template('borrower.html')
    return HttpResponse(template.render())

def lender(request):
    template = loader.get_template('lender.html')
    return HttpResponse(template.render())

def property(request):
    template = loader.get_template('property.html')
    return HttpResponse(template.render())

def colender(request):
    template = loader.get_template('colender.html')
    return HttpResponse(template.render())

def gurrantor(request):
    template = loader.get_template('gurrantor.html')
    return HttpResponse(template.render())

def form_menu(request):
    template = loader.get_template('form_menu.html')
    return HttpResponse(template.render())

@csrf_exempt
def add_borrower(request):
    if request.method == "POST":
        data = request.POST

        name = data.get('name')
        street_address1 = data.get('street_address1')
        city = data.get('city')
        state = data.get('state')
        zip_code = data.get('zip')
        email = data.get('email')
        phone = data.get('phone')
        signer = data.get('signer')
        title = data.get('title')

        try:
            borrower = Borrower.objects.create(
                name=name,
                street_address1=street_address1,
                city=city,
                state=state,
                zip=zip_code,
                email=email,
                phone=phone,
                signer=signer,
                title=title
            )
            borrower.save()
            return render(request, 'greetings.html', {'name': 'Borrower'})
        except Exception as e:
            return HttpResponse(f"Error: {e}", status=400)

    return HttpResponse("Invalid request method", status=405)


@csrf_exempt   
def add_lender(request):
    if request.method == "POST":
        data = request.POST

        name = data.get('name')
        street_address1 = data.get('street_address1')
        street_address2 = data.get('street_address2')
        city = data.get('city')
        state = data.get('state')
        zip_code = data.get('zip')
        email = data.get('email')
        phone = data.get('phone')

        try:
            lender = Lender.objects.create(
                name=name,
                street_address1=street_address1,
                street_address2=street_address2,
                city=city,
                state=state,
                zip=zip_code,
                email=email,
                phone=phone
            )
            lender.save()
            return render(request, 'greetings.html', {'name': 'Lender'})
        except Exception as e:
            return HttpResponse(f"Error: {e}", status=400)

    return HttpResponse("Invalid request method", status=405)


@csrf_exempt
def add_property(request):
    if request.method == "POST":
        data = request.POST

        loan_number = data.get('loan_number')
        street_address = data.get('street_address')
        city = data.get('city')
        state = data.get('state')
        zip_code = data.get('zip')
        interest_rate = data.get('interest_rate')
        loan_amount = data.get('loan_amount', 0)
        rehab_withhold = data.get('rehab_withhold')
        funding_date = data.get('funding_date')   
        maturity_date = data.get('maturity_date') 
        monthly_payment = data.get('monthly_payment') 
        default_rate = data.get('default_rate')

        text_representation = num2words(loan_amount)
        #words = text_representation.split()
        #words = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        try:
            property = Property.objects.create(
                loan_number=loan_number,
                street_address=street_address,
                city=city,
                state=state,
                zip=zip_code,
                interest_rate=interest_rate,
                loan_amount=loan_amount,
                text_representation = text_representation,
                rehab_withhold=rehab_withhold,
                funding_date=funding_date,
                maturity_date=maturity_date,
                monthly_payment=monthly_payment,
                default_rate=default_rate,
            )
            property.save()
            return render(request, 'greetings.html', {'name': 'Property'})
        except Exception as e:
            return HttpResponse(f"Error: {e}", status=400)

    return HttpResponse("Invalid request method", status=405)



@csrf_exempt   
def add_colender(request):
    if request.method == "POST":
        data = request.POST

        name = data.get('name')
        street_address1 = data.get('street_address1')
        city = data.get('city')
        state = data.get('state')
        zip_code = data.get('zip')
        email = data.get('email')
        phone = data.get('phone')

        try:
            colender = CoLender.objects.create(
                name=name,
                street_address1=street_address1,
                city=city,
                state=state,
                zip=zip_code,
                email=email,
                phone=phone
            )
            colender.save()
            return render(request, 'greetings.html', {'name': 'Co-Lender'})
        except Exception as e:
            return HttpResponse(f"Error: {e}", status=400)

    return HttpResponse("Invalid request method", status=405)


@csrf_exempt   
def add_gurrantor(request):
    if request.method == "POST":
        data = request.POST

        name = data.get('name')
        street_address1 = data.get('street_address1')
        city = data.get('city')
        state = data.get('state')
        zip_code = data.get('zip')
        email = data.get('email')
        phone = data.get('phone')

        try:
            gurrantor = Gurrantor.objects.create(
                name=name,
                street_address1=street_address1,
                city=city,
                state=state,
                zip=zip_code,
                email=email,
                phone=phone
            )
            gurrantor.save()
            return render(request, 'greetings.html', {'name': 'Gurrantor'})
        except Exception as e:
            return HttpResponse(f"Error: {e}", status=400)

    return HttpResponse("Invalid request method", status=405)
