from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, related_name = 'profile')
    title = models.CharField(max_length = 100)
    descriptions = models.TextField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
