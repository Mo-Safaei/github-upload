from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
	path('', views.index, name='index'),
	path('singers/', views.singers, name='singers'),
    path('new_singer/', views.new_singer, name='new_singer'),
	path('singer/<int:singer_id>/', views.songs, name='songs'),
    path('new_song/', views.new_song, name='new_song'),
    path('songs_info/<int:song_id>/', views.songs_info, name='songs_info'),
    path('edit_song/<int:song_id>/', views.edit_song, name='edit_song'),
    path('delete_song/<int:song_id>/', views.delete_song, name='delete_song'),

]