from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('login', views.login, name="adminlogin"),
    path('autheticate', views.autheticate, name='autheticate'),
    path('signout', views.logout, name="signout"),
    path('dashboard', views.index, name='dashboard'),
]
