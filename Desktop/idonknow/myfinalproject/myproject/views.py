from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def display(request):
    fullname = request.POST['fullname']
    description = request.POST['description']
    businesswebsite = request.POST['businesswebsite']
    businesscontact = request.POST['businesscontact']
    businesslocation = request.POST['businesslocation']
    yearsofexperience = request.POST['yearsofexperience']
    
    return render(request, 'display.html', {'description':description, 'fullname':fullname, 'businesswebsite':businesswebsite, 'businesscontact':businesscontact, 'businesslocation':businesslocation, 'yearsofexperience':yearsofexperience})

