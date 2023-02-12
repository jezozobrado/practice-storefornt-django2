from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name='cart'),
    path('detail/', views.detail, name='detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
