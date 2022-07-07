from atexit import register
from django.urls import path
from .import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.registerUser,name='register'),
    path('main/',views.main,name='main'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'),name='logout'),
]
