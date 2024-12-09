from django.urls import path
from .views import process_form, main_menu

urlpatterns = [
    path('document/', process_form, name='generate_document'),
    path('', main_menu),
    
]