from django import forms
from .models import Singer, Song

class SingerForm(forms.ModelForm):
	class Meta:
		model = Singer
		fields = ['name']
		labels = {'text':''}
##########################################
class SongForm(forms.ModelForm):
	class Meta:
		model = Song
		fields = ['song_name', 'singer_id','singer_name','Composer','Released','Album','Songwriter','Lyrics']
		labels = {'text':''}
















