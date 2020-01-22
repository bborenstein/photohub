from django.db import models
# Import Datetime Package for Hire_Date attribute
from datetime import datetime
# Create Model/Schema to Migrate to Postgresql myblog database
# Allows Different Photographers to Post Own Postings

class Photographer(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    about_me = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name