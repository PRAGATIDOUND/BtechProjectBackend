from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=5000)
    description = models.TextField()

    def __str__(self):
        return self.title

class Images(models.Model):
    url = models.CharField(max_length=5000)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title        
