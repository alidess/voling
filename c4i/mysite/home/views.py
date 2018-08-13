from django.shortcuts import render

from home import models
from .models import Student
from .form import SchoolForm
# Create your views here.


def index(request):
    x = 'var'
    return render(request, "index.html", {'x': x})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def base(request):
    return render(request, "base.html")


def student(request):
    x = Student.objects.all()
    return render(request, "student.html", {'x': x})


def school_add(request):
    form = SchoolForm()
    return render(request, 'school_add.html', {'form': form})
