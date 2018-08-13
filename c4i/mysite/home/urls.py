from django.urls import path
from home import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('base/', views.base, name="base"),
    path('student/', views.student, name="student"),
    path('add/', views.school_add, name="add"),
]
