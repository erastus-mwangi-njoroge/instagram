from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = CloudinaryField('post/photos')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

def __str__(self):
        """Return title and username"""
        return "{} by @{}".format(self.title, self.profile.user)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = CloudinaryField('post/pictures')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username
