from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):

    user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)

    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Notice(models.Model):
    CATEGORY_CHOICES = [
        ("academic", "Academic"),
        ("exam", "Exam"),
        ("general", "General"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
    max_length=20,
    choices=CATEGORY_CHOICES,
    default="academic"
)
    image = models.URLField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    image = models.URLField(blank=True)

    def __str__(self):
        return self.title


class StudyMaterial(models.Model):
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='study_materials/')
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LostFound(models.Model):

    STATUS_CHOICES = [
        ("lost", "Lost"),
        ("found", "Found"),
    ]

    item_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    image = models.URLField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name
class Calendar(models.Model):

    CATEGORY_CHOICES = [
        ("exam", "Exam"),
        ("holiday", "Holiday"),
        ("semester", "Semester"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.title