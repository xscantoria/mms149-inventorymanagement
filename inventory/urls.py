from django.contrib import admin
from django.urls import path, include
from . import views
from user import views as user_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.service_list, name='service_list'),
    path('clients/', views.clients, name='clients'),
    path('suppliers/', views.suppliers, name='suppliers'), 
    path('materials/', views.materials, name='materials'),
    path('orders/', views.place_order, name='place_order'),
    path('order_success/', views.order_success, name='order_success'),
    path('inventory/', views.inventory, name='inventory'),
    path('admin/', admin.site.urls),
    path('register/', user_view.register, name='user-register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # Add more URLs for other functionalities
]

