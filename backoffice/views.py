from django.shortcuts import render


#dashboard
def index(request):
    return render(request, 'backend/dashboard.html')
