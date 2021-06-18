from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    created_at =models.DateTimeField(auto_now_add=True)
    cover_art =models.CharField(max_length=255)

    # {
    #     title: "Truth and Soul",
    #     artist: "Fishbone",
    #     created_at: "2009-06-15T13:45:30",
    #     cover_art: "http://www.google.com/coverart.jpeg"
    # }

