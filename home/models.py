from tkinter.constants import CASCADE

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='no information')
    image = models.ImageField(upload_to='sport', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name