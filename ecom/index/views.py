from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html')


def about(request):
    return render(request, 'about/about.html')


def contact(request):
    return render(request, 'contact/contact.html')

# Create your views here.
