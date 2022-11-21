from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length= 60)
    address = models.CharField(max_length= 200)
    nationality = models.CharField(max_length= 200, default= '')
    gender = models.CharField(max_length= 200, default= '')
    pix = models.ImageField(upload_to= 'Profile', default='profile.jpg')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'profile'
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

