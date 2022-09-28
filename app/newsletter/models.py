from enum import unique
from pickle import TRUE
from tkinter import Widget
from django.db import models
from pkg_resources import require
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class RegisteredUser(models.Model):
    name = models.CharField(max_length=40)
    phone = PhoneNumberField(unique=True)
    created = models.DateTimeField(auto_now_add=True)    #auto_now_add sets datetime to when created, not when updated

    class Meta:
        ordering = ['-created'] # makes the ordering descending by date for the dashboard

    def __str__(self):
        return self.name