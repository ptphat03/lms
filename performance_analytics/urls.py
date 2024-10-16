from django.urls import path,include
from django.urls import path
from user_summary import views
app_name = 'performance_analytics'

urlpatterns = [
    path('',views.user_summary, name='performance_list')
    
    
]