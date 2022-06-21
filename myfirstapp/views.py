from django.shortcuts import render
from myfirstapp.models import Webpage, User
from myfirstapp.forms import UserForm


def index(request):
    form = UserForm(request.POST)

    qs_webpages = Webpage.objects.filter(url__contains='https')
    qs_users = User.objects.all()
    values = {
        "test_variable": "From views.py!",
        "webpage_records": qs_webpages,
        "user_records": qs_users,
        "form": form
    }

    if request.method == 'POST':
        if form.is_valid():
            print("Valid data!")
            print(f'First name: {form.cleaned_data["first_name"]} | Last name: {form.cleaned_data["last_name"]} | email: {form.cleaned_data["email"]}')

    return render(request, 'myfirstapp/index.html', context=values)
