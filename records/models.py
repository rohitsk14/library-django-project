from django.db import models
from datetime import datetime
# Create your models here.
class record(models.Model):
    book_id = models.CharField(max_length=10, default='')
    student_id = models.CharField(max_length=15,default='')
    student_name = models.CharField(max_length=30, default='')
    year = models.CharField(max_length=10, default='')
    issue_date = models.CharField(max_length=20,null=True)
    return_date = models.CharField(max_length=20,default="",null=True)