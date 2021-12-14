import datetime

from django.db import models


# Create your models here.


class Driver(models.Model):
    first_name = models.CharField('Driver`s first name', max_length=30)
    last_name = models.CharField('Driver`s last name', max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.last_name


class Vehicle(models.Model):
    driver_id = models.IntegerField()
    make = models.CharField('Car brand', max_length=30)
    model = models.CharField('Car model', max_length=30)
    plate_number = models.CharField('Car plates', max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.model
