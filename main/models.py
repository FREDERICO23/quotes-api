from django.db import models

class Quote(models.Model):
    quote = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    
class Author(models.Model):
    name = models.CharField(max_length=100)