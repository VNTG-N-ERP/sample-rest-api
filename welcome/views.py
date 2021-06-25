from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render


# Create your views here.
def hello_world(request):
    return render(request, 'welcome/hello_world.html')
