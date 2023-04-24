from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profile (models.Model):
    staff = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    address =models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    image = models.ImageField(default='avater.jpg',upload_to='profile_images')

    
    def __str__(self):
        return f'{self.staff.username}-Profile'

class Position(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Candidate(models.Model):
    name = models.CharField(max_length=50)
    total_vote = models.IntegerField(default=0, editable=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Candidate Pic", upload_to='images/')

    def __str__(self):
        return "{} - {}".format(self.name, self.position.title)


class ControlVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.position, self.status)



class comment(models.Model): # new
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    text = models.TextField()

    
    def __str__(self): # new
        return self.subject[:50]
