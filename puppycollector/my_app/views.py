# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Puppy

# View for home page
def home(request):
    return HttpResponse('<h1>Hello Puppy Collector</h1>')

# View for about page
def about(request):
    return render(request, 'about.html')

# View for puppy index page
def puppy_index(request):
    puppies = Puppy.objects.all()  # Fetch all puppies from the database
    return render(request, 'puppies/index.html', {'puppies': puppies})

# View for puppy detail page
def puppy_detail(request, puppy_id):
    puppy = Puppy.objects.get(id=puppy_id)  # Fetch puppy by ID
    return render(request, 'puppies/detail.html', {'puppy': puppy})
