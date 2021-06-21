from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm
# from .models import Artist
# from .artist_form import ArtistForm

# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": albums})

### artists
# def list_artists(request):
#     artists = Artist.objects.all()
#     return render(request, "albums/list_artists.html",
#                   {"artists": artists})

# def add_aritst(request):
#     if request.method == 'GET':
#         form_2 = ArtistForm()
#     else:
#         form_2 = ArtistForm(data=request.POST)
#         if form_2.is_valid():
#             return redirect(to='list_artists')
#     return render(request, "albums/add_artist.html", {"form": form_2})

#########

def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            return redirect(to='list_albums')
    return render(request, "albums/add_album.html", {"form": form})



def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_album.html", {
        "form": form,
        "album": album
    })


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_album.html",
                  {"album": album})



def show_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/show_album.html",
                  {"album": album})

