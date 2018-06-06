from django.db import models
from django.utils import timezone



# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length = 400)
    text = models.TextField()
    created = models.DateField(default = timezone.now())
    photo = models.ImageField(upload_to='images',blank =True,null=True)
