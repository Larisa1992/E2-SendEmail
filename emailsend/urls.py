from django.urls import path
from .views import index, success


app_name = 'emailsend'
urlpatterns = [
    path('', index, name='contact'),
    path('success/', success, name='success'),
]