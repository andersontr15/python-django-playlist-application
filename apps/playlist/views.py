from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from apps.playlist.models import User, Song, Playlist
from django.utils import timezone
from datetime import datetime


def index(request):
	print request.GET
	print request.method
	return render(request, 'playlist/index.html')

def register(request):
	print "Registration"
	user = User.objects.filter(email= request.POST.get('email'), password=request.POST.get('password'))
	if len(user) > 0 and len(request.POST.get('email'))<3:
		return redirect('/')
	else:
		user = User()
		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		user.email = request.POST.get('email')
		user.password = request.POST.get('password')
		user.save()
		print "Successful Registration"
		print user.first_name
		print user.last_name
		print user.email
		print user.password
		return redirect('/')

def login(request):
	print "Login"
	print request.POST.get('email')
	print request.POST.get('password')
	user = User.objects.filter(email=request.POST.get('email'))
	if len(user)<1:
		print "Failed"
		return redirect('/')
	else:
		print "Success"
		request.session['user_id'] = user[0].id
		print "Logging In.."
		return redirect('/dashboard')

def dashboard(request):
	print "User Dashboard"
	if "user_id" in request.session:
		songs = Song.objects.all().order_by('counter').reverse
		user = User.objects.get(id=request.session['user_id'])
		context = {
			'user': user,
			'songs': songs,
		}
		return render(request, 'playlist/dashboard.html', context)
	else:
		del request.session
		return redirect('/')

def add_song(request):
	print "Adding a song"
	song = Song()
	print request.POST.get('title')
	print request.POST.get('artist')
	song.title = request.POST.get('title')
	song.artist = request.POST.get('artist')
	song.created_at = timezone.now()
	song.counter = 0
	if len(song.title) < 2 or len(song.artist) < 2:
		return redirect('/dashboard')
	else:
		song.save()
		return redirect('/dashboard')

def user(request, user_id):
	print "in user"
	user = User.objects.get(id=user_id)
	song = Song.objects.all()
	songs = Playlist.objects.all().filter(user=user).filter(song=song).order_by('counter')
	context = {
	'user': user,
	'songs': songs,
	}
	return render(request, 'playlist/profile.html', context)

def song(request, song_id):
	print "Viewing song"
	song = Song.objects.get(id=song_id)
	playlists = Playlist.objects.all().filter(song=song).exclude(user=request.session['user_id'])
	context = {
	'playlists': playlists,
	'song': song,
	}
	return render(request, 'playlist/song.html', context)

def add_playlist(request, song_id):
	song = Song.objects.get(id=song_id)
	user = User.objects.get(id=request.session['user_id'])
	counter = 0
	p = Playlist()
	p.user = user
	p.song = song
	p.counter = counter+1
	p.save()
	print p.user.first_name
	song.counter+=1
	song.save()
	return redirect('/dashboard')

def logout(request):
	print "Logging Out"
	del request.session['user_id']
	return redirect('/')