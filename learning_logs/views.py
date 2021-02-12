from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Singer
from .forms import SingerForm, SongForm
from django.http import Http404
from django.contrib.auth.decorators import login_required


##################################################################
##################################################################

def index(request):
    return render(request, 'learning_logs/index.html')


##################################################################
##################################################################

# @login_required
def singers(request):
    singers = Singer.objects.order_by('date_added')
    context = {'singers': singers}
    return render(request, 'learning_logs/singers.html', context)


##################################################################
##################################################################
# @login_required
def new_singer(request):
    if request.method != 'POST':
        form = SingerForm()
    else:
        form = SingerForm(data=request.POST)
        if form.is_valid():
            new_singer = form.save(commit=False)
            new_singer.owner = request.user
            new_singer.save()
            return redirect('learning_logs:singers')

    context = {'form': form}
    return render(request, 'learning_logs/new_singer.html', context)


##################################################################
##################################################################
# @login_required
def songs(request, singer_id):
    song = Song.objects.filter(singer_id_id=singer_id)

    context = {'songs': song}
    return render(request, 'learning_logs/songs.html', context)


##################################################################
##################################################################
# @login_required
def new_song(request):
    if request.method != 'POST':
        form = SongForm()
    else:
        form = SongForm(data=request.POST)
        if form.is_valid():
            new_song = form.save(commit=False)
            new_song.owner = request.user
            new_song.save()
            return redirect('learning_logs:singers')

    context = {'form': form}
    return render(request, 'learning_logs/new_song.html', context)


##################################################################
##################################################################

# @login_required
def songs_info(request, song_id):
    song = Song.objects.filter(id=song_id)

    context = {'songs_Info': song}
    return render(request, 'learning_logs/songs_info.html', context)


##################################################################
##################################################################
# @login_required
def edit_song(request, song_id):
    song = Song.objects.get(id=song_id)

    if song.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = SongForm(instance=song)
    else:
        form = SongForm(instance=song, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:songs_info', song_id=song.id)
    context = {'song': song, 'form': form}
    return render(request, 'learning_logs/edit_song.html', context)


##################################################################
##################################################################
def delete_song(request, song_id):
    song = Song.objects.get(id=song_id)
    if song.owner != request.user:
        raise Http404

    song.delete()
    return redirect('learning_logs:singers')


##################################################################
##################################################################

