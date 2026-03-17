from django.urls import path
from . import views

urlpatterns = [
    path('', views.savinggold_page, name='savinggold'),
    path('search/', views.search, name='search'),
    path('saleexport/', views.saleexport, name='saleexport'),
]
