from django.db import models
from django.contrib.auth.models import User

class Singer(models.Model):
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.name

############################################################################
class Song(models.Model):
	"""Something specific learned about a topic."""
	singer_id = models.ForeignKey(Singer, on_delete=models.SET_NULL, null=True)
	song_name = models.CharField(max_length=200)
	singer_name = models.CharField(max_length=200,blank=True,null=True)
	Released = models.CharField(max_length=200,blank=True,null=True)
	Album = models.CharField(max_length=200,blank=True,null=True)
	Songwriter = models.CharField(max_length=200,blank=True,null=True)
	Composer = models.CharField(max_length=200,blank=True,null=True)
	Lyrics = models.TextField(blank=True,null=True)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.song_name





