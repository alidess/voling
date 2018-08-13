from django.db import models

# Create your models here.

"""
class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    birth_date = models.DateField(null=False)
"""


class Cat(models.Model):
    type = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.type


class Movies(models.Model):
    title = models.CharField(max_length=150)
    year = models.DateField(null=False)
    desc = models.CharField(max_length=200)
    pic = models.ImageField
    link = models.CharField(max_length=200)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class School(models.Model):
    school_name = models.CharField(max_length=40)
    found_date = models.DateField(null=False)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.school_name


class City(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Grade(models.Model):
    my_grade = models.CharField(max_length=200)

    def __str__(self):
        return self.my_grade


class Student(models.Model):
    st_name = models.CharField(max_length=40)
    age = models.IntegerField()
    birthdate = models.DateField(null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.st_name
