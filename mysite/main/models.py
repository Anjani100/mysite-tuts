from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length = 200)
	tutorial_published = models.DateTimeField("date published", default = datetime.now())
	tutorial_content = models.TextField()

	def __str__(self):
		return self.tutorial_title

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()