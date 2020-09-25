from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Customer, Service, ServiceCategory, ServiceSubCategory, Booking, IndexPage


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
    return render(request, 'frontend/help.html')


#booking-page
def bookingPage(request):
    return render(request, 'frontend/booking_page.html')


#register
def register(request):
    """
    Register user
    """
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        phone_no = request.POST['phone_no']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The email is already registered')
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(
                        request, 'You are now registered. You can proceed to login')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'frontend/register.html')


#login
def login(request):
    """ view for login """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('booking_page')

        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    else:
        return render(request, 'frontend/login.html')


#myaccount
def myAccount(request):
    customer = Customer.objects.all()

    context = {
        'customer': customer
    }

    return render(request, 'frontend/myaccount.html', context)


#register
def logout(request):
    return redirect('index')
