from django.db import models

class Item(models.Model):
    '''list element'''
    text = models.TextField(default='')

# Create your models here.
