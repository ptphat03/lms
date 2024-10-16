from django.urls import path
from user_summary import views

app_name = 'user_progress'

urlpatterns = [
    path('',views.user_summary, name='progress_list')
]