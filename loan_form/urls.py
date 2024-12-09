from django.contrib import admin
from django.urls import path, include
from .views import borrower, lender, colender, property, gurrantor, add_borrower, add_colender, add_gurrantor, add_lender, add_property, form_menu

urlpatterns = [
    path('borrower/', borrower),
    path('lender/', lender),
    path('colender/', colender),
    path('property/', property),
    path('gurrantor/', gurrantor),
    path('add-property', add_property),
    path('add-borrower/', add_borrower),
    path('add-colender/', add_colender),
    path('add-gurrantor/', add_gurrantor),
    path('add-lender/', add_lender),
    path('greetings/', add_lender),
    path('', form_menu),
]
