from django.shortcuts import render


#Home page
def index(request):
    return render(request, 'frontend/index.html')


#Salon
def salon(request):
    return render(request, 'frontend/salon.html')


#Barber
def barber(request):
    return render(request, 'frontend/barber.html')


#serviceCategories
def serviceCategories(request):
    return render(request, 'frontend/service_categories.html')


#serviceSubCategories
def serviceSubCategories(request):
    return render(request, 'frontend/service_subcategories.html')


#servicedetails
def serviceDetails(request):
    return render(request, 'frontend/service_details.html')


#myaccount
def myAccount(request):
    return render(request, 'frontend/myaccount.html')


#help
def help(request):
    return render(request, 'frontend/help.html')
