from django.db import models
from django.utils import timezone

# Create your models here.



class Enquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    add_date = models.DateTimeField('date added')
    def __str__(self):
        return self.name
