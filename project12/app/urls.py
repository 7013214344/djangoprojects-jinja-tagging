from django.urls import path
from app.views import *

urlpatterns = [
    path('login/',login,name='login'),  
    path('registration/',registration,name ='registration'),

    
]