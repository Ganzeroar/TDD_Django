from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    '''home_page'''
    return render(request, 'home.html')