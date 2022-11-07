from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('kril', kril, name="kril"),
    path('lotin', lotin, name="lotin"),
    path('latin/', latin, name="latin"),
]
