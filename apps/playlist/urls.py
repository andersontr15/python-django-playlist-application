from django.conf.urls import patterns, url
from apps.playlist import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'register$', views.register, name="register"),
	url(r'login$', views.login, name="login"),
	url(r'dashboard$', views.dashboard, name="dashboard"),
	url(r'logout$', views.logout, name="logout"),
	url(r'add_song$', views.add_song, name="add_song"),
	url(r'^song/(?P<song_id>\d+)/$', views.song, name="song"),
	url(r'^song/(?P<song_id>\d+)/add_playlist$', views.add_playlist, name="add_playlist"),
	url(r'^user/(?P<user_id>\d+)/$', views.user),

)