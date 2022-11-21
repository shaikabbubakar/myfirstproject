from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def good(request):
    return HttpResponse('<h2>hai hello goodmorning to all how are u</h2>')