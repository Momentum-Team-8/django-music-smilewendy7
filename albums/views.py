from django.shortcuts import render
from .models import Album

# Create your views here.
def list_ablums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": albums})


