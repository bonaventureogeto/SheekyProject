from django.urls import path
from .views import authentication

app_name = 'app'
urlpatterns = [
    path('login', authentication.login, name="adminlogin"),
    path('autheticate', authentication.autheticate, name='autheticate'),
    path('signout', authentication.logout, name="signout"),
    path('dashboard', authentication.index, name='dashboard'),
]
