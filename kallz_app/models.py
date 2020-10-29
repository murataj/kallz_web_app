from django.db import models
from django.utils import timezone
from phone_field import PhoneField

class User(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Professor(models.Model):
    CATEGORY = (
        ('IT Teacher', 'IT Teacher'),
        ('Foreign Languages Teacher', 'Foreign Languages Teacher'),
        ('Social Science Teacher', 'Social Science Teacher'),
        ('Science Teacher', 'Science Teacher'),
    )

    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    birthday = models.DateTimeField(input, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    #number_of_courses = models.IntegerField()
    email = models.EmailField(max_length=50, null=True)
    phone = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    CATEGORY = (
        ('Kids 8-12 years', 'Kids 8-12 years'),
        ('Teenagers 13-18 years old', 'Teenagers 13-18 years old'),
        ('Adults older than 19', 'Adults older than 19'),
    )

    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    birthday = models.DateTimeField(input, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    #number_of_courses = models.IntegerField()
    email = models.EmailField(max_length=50, null=True)
    phone = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    STATUS = (
        ('On going', 'On going'),
        ('New course', 'New course'), 
        ('To be out soon', 'To be out soon'),
    )

    course_name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_started = models.DateTimeField(input, null=True )
    date_ended = models.DateTimeField(input, null=True )
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    description = models.CharField(max_length=500, null=True)
 
    def __str__(self):
        return self.course_name

class InteractiveClass(models.Model):
    
    students = models.ManyToManyField(Student)
    professor = models.OneToOneField(Professor, null=True, on_delete=models.SET_NULL)
    course = models.OneToOneField(Course, null=True, on_delete =  models.SET_NULL)
    class_name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_time_started = models.DateTimeField(input, null=True )
    date_time_ended = models.DateTimeField(input, null=True )
    description = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.class_name
    

