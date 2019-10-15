from django.db import models

# Create your models here.
class books(models.Model):
    book_id = models.CharField(max_length=10, default='')
    title=models.CharField(max_length=30,default='')
    author = models.CharField(max_length=30, default='')
    publisher = models.CharField(max_length=30, default='')
    rack_no = models.CharField(max_length=5, default='')
    no_of_copies = models.IntegerField()
