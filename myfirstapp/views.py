from django.shortcuts import render
from django.contrib import messages
from myfirstapp.models import Webpage, User
from myfirstapp.forms import UserForm


def index(request):
    qs_webpages = Webpage.objects.filter(url__contains='https')
    qs_users = User.objects.all()
    values = {
        "test_variable": "From views.py!",
        "webpage_records": qs_webpages,
        "user_records": qs_users
    }

    return render(request, 'myfirstapp/index.html', context=values)


def user_form_view(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print("Valid data!")
            print(f'First name: {form.cleaned_data["first_name"]} | Last name: {form.cleaned_data["last_name"]} | email: {form.cleaned_data["email"]}')
            messages.success(request, 'Success.')
            form.save(commit=True)
            return index(request)
        else:
            messages.error(request, 'Error.')
            print("Error")

    return render(request, 'myfirstapp/form_page.html', {'form': form})
