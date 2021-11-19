from django.db import models
import uuid

# Create your models here.
# Main Model
class HomePageModel(models.Model):
    music_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    artist = models.CharField(max_length=200)
    album_name = models.CharField(max_length=200, default='Single')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    audio_file = models.FileField(blank=True, null=True, upload_to='musics/')
    audio_link = models.CharField(max_length=1200,blank=True,null=True)
    playlist = models.ManyToManyField('PlayList')
    category = models.ManyToManyField('Category')
    lyrics = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.music_name

    class Meta:
        ordering = ['-created']



# PlayLists
class PlayList(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name



# Categories
class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
