from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# myapp/views.py
from django.shortcuts import render
from .models import UserData
from django.http import HttpResponse

def submit_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # Save the data to the database
        user = UserData(name=name, email=email)
        user.save()
        return HttpResponse('Data submitted successfully!')
    return render(request, 'form.html')


def home(request):
    return HttpResponse("Hello, Loki!")
