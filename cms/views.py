from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Customer, Department, Service, Product, ServiceCategory, ServiceSubCategory, Booking, IndexPage, Help


#Home page
def index(request):
    """ view for index/home page"""
    index = IndexPage.objects.all()

    context = {
        'index': index
    }

    return render(request, 'frontend/index.html', context)


#Salon
def salon(request):
    """ view for salon"""
    service_category = ServiceCategory.objects.all()

    context = {
        'service_category': service_category
    }

    return render(request, 'frontend/salon.html', context)


#Barber
def barber(request):
    """ view for barber"""
    service_category = ServiceCategory.objects.all()

    context = {
        'service_category': service_category
    }

    return render(request, 'frontend/barber.html', context)


#products
def products(request):
    """ view for products"""
    product = Product.objects.all()

    context = {
        'product': product
    }

    return render(request, 'frontend/products.html', context)


#serviceCategories
def serviceCategories(request):
    """ view for service categories page"""
    service_subcategory = ServiceSubCategory.objects.all()

    context = {
        'service_subcategory': service_subcategory
    }

    return render(request, 'frontend/service_categories.html', context)


#serviceSubCategories
def serviceSubCategories(request):
    """ view for service subcategories page """
    service = Service.objects.all()

    context = {
        'service': service
    }

    return render(request, 'frontend/service_subcategories.html', context)


#servicedetails
def serviceDetails(request):
    """ view for service details page """
    service = Service.objects.all()

    context = {
        'service': service
    }
    
    return render(request, 'frontend/service_details.html', context)


#help
def help(request):
    """ view for help page """
    help = Help.objects.all()

    context = {
        'help': help
    }

    return render(request, 'frontend/help.html', context)


#booking-page
def bookingPage(request):
    """ views for booking """
    time = Booking.objects.all()

    if request.method =='POST':
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        user_id = request.user.id

        booking = Booking(appointment_date=appointment_date, appointment_time=appointment_time, user_id=user_id)

        # check if user is logged in in order to book.
        if request.user.is_authenticated:
            booking.save()

            messages.success(
                request,
                "We can't wait to meet you :) Your appointment with us has been confirmed. You get 200 points worth KSH. 200 for booking your first appointment. If you show up on time you could win yourself a free facial. Please remember to wear your face mask. See You Then."
            )
        else:
            return render(request, 'frontend/accounts/login.html')

    return render(request, 'frontend/booking_page.html')
