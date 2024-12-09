from django.contrib import admin
from django.urls import path, include, re_path
from generator.views import main_menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', include('loan_form.urls')),
    path('generate/', include('generator.urls')),
    re_path(r'^(?!admin|form|generate).*$', main_menu), 
]
