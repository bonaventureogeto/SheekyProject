from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Customer, Service, ServiceCategory, ServiceSubCategory, Booking, SheekyHub, ContactUs, AboutUs


#Home page
def index(request):
    return render(request, 'frontend/index.html')


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


# def service(request, service_id):
#     service = get_object_or_404(Service, pk=service_id)

#     context = {
#         'service': service
#     }

#     return render(request, 'frontend/service_details.html', context)


#myaccount
def myAccount(request):
    customer = Customer.objects.all()

    context = {
        'customer': customer
    }

    return render(request, 'frontend/myaccount.html', context)


#help
def help(request):
    return render(request, 'frontend/help.html')


#booking-page
def bookingPage(request):
    return render(request, 'frontend/booking_page.html')


#register
def register(request):
    return render(request, 'frontend/register.html')


#login
def login(request):
    """ view for login """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')

        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    else:
        return render(request, 'frontend/login.html')
