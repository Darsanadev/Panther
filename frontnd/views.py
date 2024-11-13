from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def team(request):
    return render(request, 'Team.html')

def gallary(request):
    
    return render(request, 'gallary.html')

def res(request):
    return render(request, 'res.html')

