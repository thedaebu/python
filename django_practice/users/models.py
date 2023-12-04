from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/profile2.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
