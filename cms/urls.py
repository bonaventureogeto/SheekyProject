from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salon', views.salon, name='salon'),
    path('barber', views.barber, name='barber'),
    path('products', views.products, name='products'),
    path('doorstepdeluxe', views.doorstepdeluxe, name='doorstepdeluxe'),
    path('service-categories', views.serviceCategories, name='service_categories'),
    path('service-subcategories', views.serviceSubCategories, name='service_subcategories'),
    path('service-details', views.serviceDetails, name='service_details'),
    path('help', views.help, name='help'),
    path('sheekyhub', views.sheekyhub, name='sheekyhub'),
    path('booking-page', views.bookingPage, name='booking-page'),
]
