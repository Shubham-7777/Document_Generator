from django.urls import path
from .views import upload_excel, select_lender_borrower

urlpatterns = [
    path('upload_excel/', upload_excel, name='upload_excel'),
    path('select_lender_borrower/', select_lender_borrower, name='select_lender_borrower'),
]
