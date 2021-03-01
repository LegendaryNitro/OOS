from django.urls import include, path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',register, name='register'),
    path('home/',home, name='home'),
    path('profile/',profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name=f'{ff}/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name=f'{ff}/logout.html'), name='logout'),
]