from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.core.validators import ValidationError
from django.core.validators import EmailValidator

class Detail(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField(default=0)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Contact(models.Model):
    def min_length_check(val):
        if len(val) < 10:
            raise ValidationError('Value must should be Greater than 10')
    # def emailvalidate(self):
    #     raise EmailValidator('Email should be with @, letter and character')

    a = models.CharField(validators=[min_length_check], max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    Images = models.FileField(upload_to='zymlover/', null=True)
    b = models.EmailField(max_length=100, default=0, null=True)
    c = models.CharField(max_length=500)

    def __str__(self):
        return self.a

class Book(models.Model):
    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('p', 'Publishes'),
        ('w', 'Withdrawn')
    ]
    id = models.AutoField(primary_key=True)
    names = models.CharField(max_length=20)
    emails = models.EmailField(max_length=100, default=0, null=True)
    phones = models.IntegerField()
    addresses = models.CharField(max_length=300)
    fnames = models.CharField(max_length=20)
    mnames = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    fees = models.IntegerField()
    statuses = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    def __str__(self):
        return self.names

    def show_emails(self):
        return self.emails
    show_emails.short_description = 'Book Emails'

    class Meta:
        db_table = 'Books'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


