from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse


# Create your models here.

# Create User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)
    img = models.ImageField(max_length=1000, default=" ")


    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


#def create_profile(sender, **kwargs):
 #   if kwargs['created']:
  #      user_profile = UserProfile.objects.create(user=kwargs['instance'])


# linking between userProfile and User
#post_save.connect(create_profile, sender=User)



# create actor
class Actor(models.Model):
    name = models.CharField(max_length=250, default=" ")
    birthdate = models.CharField(max_length=300, default="1/1")
    socialMedia = models.CharField(max_length=250, default=" ")
    image = models.ImageField(max_length=1000, default=" ")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details:actor', kwargs={'pk': self.pk})

class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'birthdate', 'socialMedia', 'image']


class Parent(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)


class Movie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=500)
    movie_date = models.CharField(max_length=250)
    movie_image = models.ImageField(max_length=1000, default=" ")

    def __str__(self):
        return self.movie_name


class Prize(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    prizeName = models.CharField(max_length=500)
    prizeDate = models.CharField(max_length=250)

    def __str__(self):
        return self.prizeName



class Review(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default='')
    def __str__(self):
        return self.user.username

class Message(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default='')
    def __str__(self):
        return self.user.username

