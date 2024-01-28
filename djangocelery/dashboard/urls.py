from django.urls import path
from dashboard import views as dashboard_views

urlpatterns = [
    path('', dashboard_views.home, name='dashboard'),
    path('generate_pdf', dashboard_views.process_pdf, name='generate_pdf'),
]