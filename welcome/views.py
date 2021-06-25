from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from decouple import config


# Create your views here.
def hello_world(request):
    db_info = {
        'name': config('POSTGRES_NAME'),
        'user': config('POSTGRES_USER'),
    }
    context = {'test_data': db_info}
    return render(request, 'welcome/hello_world.html', context)
