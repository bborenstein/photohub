from django.db import models
# Import Datetime Package for List_Date attribute
from datetime import datetime
# Import Photographer Model for Foreign Key usage
from photographers.models import Photographer


# Create Model/Schema to Migrate to Postgresql myblog database
class Posting(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    blogcopy_main = models.TextField(blank=True)
    blogcopy_1 = models.TextField(blank=True) 
    blogcopy_2 = models.TextField(blank=True)
    blogcopy_3 = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    posted_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title