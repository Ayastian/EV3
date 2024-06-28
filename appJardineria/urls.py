from django.urls import path
from . import views


urlpatterns = [
    path('productos', views.productos, name='productos'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('home', views.home, name='home'),
    path('checkout', views.checkout, name='checkout'),
]


