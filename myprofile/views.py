from django.shortcuts import render



def home(request):
    return render(request, 'myprofile/home.html')

def about(request):
    return render(request, 'myprofile/about.html')

def contact(request):
    return render(request, 'myprofile/contact.html')
