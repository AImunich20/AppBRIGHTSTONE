from django.urls import path
from . import views

urlpatterns = [
    path('', views.savinggold_page, name='savinggold'),
]