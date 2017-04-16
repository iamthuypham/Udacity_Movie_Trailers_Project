from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class Movie(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    story_line = models.TextField()
    poster_image_url = models.CharField(max_length=255)
    trailer_youtube_url = models.CharField(max_length=255)
    trailer_youtube_id = models.TextField(editable=False)
    
    def __str__(self):
        return self.title
    
    def save(self):
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', self.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', self.trailer_youtube_url)
        self.trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        super(Movie, self).save()
        # return self.trailer_youtube_id
        