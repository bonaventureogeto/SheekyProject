from django.urls import path
from .views import authentication
from .views import subcategories

app_name = 'app'
urlpatterns = [
    path('login', authentication.login, name="adminlogin"),
    path('autheticate', authentication.autheticate, name='autheticate'),
    path('signout', authentication.logout, name="signout"),
    path('dashboard', authentication.index, name='dashboard'),
    path('subcategories/index', subcategories.index, name='subcategories.index'),
    path('subcategories/create', subcategories.create, name='subcategories.create'),
]
