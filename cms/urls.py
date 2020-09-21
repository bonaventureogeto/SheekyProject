from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salon', views.salon, name='salon'),
    path('barber', views.barber, name='barber'),
    path('service-categories', views.serviceCategories, name='service_categories'),
    path('service-subcategories', views.serviceSubCategories, name='service_subcategories'),
    path('service-details', views.serviceDetails, name='service_details'),
    path('myaccount', views.myAccount, name='myaccount'),
    path('help', views.help, name='help'),
]
