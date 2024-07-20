from django.db import models
from django.utils import timezone

# Create your models here.

class prjvariety(models.Model):
    PRJ_TYPE_CHOICE = [
        ("ECOM", "ECOMMERCE"),
        ("HM", "HOSPITAL"),
        ("SM", "SOCIALMEDIA"),
        ("FT", "FITNESS")
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='prjs/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=4, choices=PRJ_TYPE_CHOICE)
    description = models.TextField(default='')
