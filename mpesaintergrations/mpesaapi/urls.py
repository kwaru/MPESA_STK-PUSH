from django.urls import path

from .views import getAccessToken,lipa_na_mpesa_online

urlpatterns = [

path('api/v1/mpesa/', getAccessToken),
path('online/lipa', lipa_na_mpesa_online, name='lipa_na_mpesa'),

]