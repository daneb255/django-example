from django.shortcuts import render
from myfirstapp.models import Webpage


def index(request):

    wp = Webpage.objects.filter(url__contains='https')
    values = {
        "test_variable": "From views.py!",
        "webpage_records": wp

    }

    return render(request, 'myfirstapp/index.html', context=values)
