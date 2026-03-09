from django.urls import path
from . import views

urlpatterns = [
    path("goldprice/", views.goldprice_api, name="goldprice_api"),
]