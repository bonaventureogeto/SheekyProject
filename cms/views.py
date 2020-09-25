from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Customer, Service, ServiceCategory, ServiceSubCategory, Booking, IndexPage, Help


#Home page
def index(request):
    index = IndexPage.objects.all()

    context = {
        'index': index
    }

    return render(request, 'frontend/index.html', context)


#Salon
def salon(request):
    service_category = ServiceCategory.objects.all()

    context = {
        'service_category': service_category
    }

    return render(request, 'frontend/salon.html', context)


#Barber
def barber(request):
    return render(request, 'frontend/barber.html')


#serviceCategories
def serviceCategories(request):
    service_subcategory = ServiceSubCategory.objects.all()

    context = {
        'service_subcategory': service_subcategory
    }

    return render(request, 'frontend/service_categories.html', context)


#serviceSubCategories
def serviceSubCategories(request):
    service = Service.objects.all()

    context = {
        'service': service
    }

    return render(request, 'frontend/service_subcategories.html', context)


#servicedetails
def serviceDetails(request):
    service = Service.objects.all()

    context = {
        'service': service
    }
    
    return render(request, 'frontend/service_details.html', context)


#help
def help(request):
    help = Help.objects.all()

    context = {
        'help': help
    }

    return render(request, 'frontend/help.html', context)


#booking-page
def bookingPage(request):
    return render(request, 'frontend/booking_page.html')

