from django.urls import path
from . import views
from user_summary import views as summary

app_name = 'certificate'

urlpatterns = [
    path('', summary.user_summary, name='certificate_list'),
    path('pdf/<int:id>/', views.certificate_pdf, name='certificate_pdf'),
]

