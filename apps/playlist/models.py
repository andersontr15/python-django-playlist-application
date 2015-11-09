from django.db import models

class User(models.Model):
	first_name = models.TextField(blank=False, max_length=20)
	last_name = models.TextField(blank=False, max_length=20)
	email = models.TextField(blank=False, max_length=20)
	password = models.TextField(blank=False, max_length=20)
	counter = models.IntegerField(blank=False, null=True)
	class Meta:
		db_table = 'user'

class Song(models.Model):
	title = models.TextField(blank=False, max_length=20)
	artist= models.TextField(blank=False, max_length=20)
	counter = models.IntegerField(blank=False, null=True)
	class Meta:
		db_table = 'songs'


class Playlist(models.Model):
	user = models.ForeignKey(User, related_name="user", null=True)
	song = models.ForeignKey(Song, related_name="song", null=True)
	counter = models.IntegerField(blank=False, null=True, default=0)
	class Meta:
		db_table = 'playlists'