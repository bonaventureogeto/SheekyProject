from django.urls import path
from .views import authentication
from .views import subcategories
from .views import categories

app_name = 'app'
urlpatterns = [
    path('login', authentication.login, name="adminlogin"),
    path('autheticate', authentication.autheticate, name='autheticate'),
    path('signout', authentication.logout, name="signout"),
    path('dashboard', authentication.index, name='dashboard'),
    path('subcategories/index', subcategories.index, name='subcategories.index'),
    path('subcategories/create', subcategories.create, name='subcategories.create'),
    path('subcategories/store', subcategories.store, name='subcategories.store'),
    path('categories/index', categories.index, name='categories.index'),
    path('categories/create', categories.create, name='categories.create'),
    path('categories/store', categories.store, name='categories.store'),
]
