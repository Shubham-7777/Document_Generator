from django.contrib import admin
from .models import Lender, Borrower, Property, CoLender, Gurrantor

class LenderAdmin(admin.ModelAdmin):
    list_display = ('name','street_address1', 'street_address2', 'city', 'state', 'zip', 'email', 'phone')

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('name','street_address1', 'city', 'state', 'zip', 'email', 'phone', 'signer', 'title')

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('loan_number','street_address', 'city', 'state', 'zip', 'interest_rate', 'loan_amount', 'text_representation', 'rehab_withhold', 'funding_date',
                    'maturity_date', 'monthly_payment', 'default_rate')

class CoLenderAdmin(admin.ModelAdmin):
    list_display = ('name','street_address1', 'city', 'state', 'zip', 'email', 'phone')
    
class GurrantorAdmin(admin.ModelAdmin):
    list_display = ('name','street_address1', 'city', 'state', 'zip', 'email', 'phone')
    


admin.site.register(Lender, LenderAdmin)
admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(CoLender, CoLenderAdmin)
admin.site.register(Gurrantor, GurrantorAdmin)