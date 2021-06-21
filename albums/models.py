from django.db import models

# Create your models here.

class Album(models.Model):
    # foreign key
    artist= models.ForeignKey(
        "Artist",
        on_delete=models.CASCADE,
        related_name="albums",
        #### this step is important!!!! means artist_id can be null.
        null=True,
    )

    title = models.CharField(max_length=255)
    created_at =models.DateTimeField(auto_now_add=False)
    cover_art =models.CharField(max_length=255)
    


class Artist(models.Model):
    artist_name = models.CharField(max_length=255)

    def __str__(self):
        #### this below fixed 
        return f"{self.artist_name}"
