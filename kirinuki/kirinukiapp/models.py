import math
from django.db import models
from django.core.validators import FileExtensionValidator
from moviepy.editor import VideoFileClip
# Create your models here.

# FileField
class FileUpload(models.Model):
        
    attach = models.FileField(
        upload_to='media/',
        verbose_name='添付ファイル',
        validators=[FileExtensionValidator(['mp3','avi', 'mp4' ])],
    )
    @property
    def filename(self):
        return self.attach.path
    @property
    def duration(self, *args, **kwargs):
        if self.attach:
            video = VideoFileClip(self.attach.path)
            video_duration = math.floor(video.duration)
        return video_duration

class GenerateGif(models.Model):
    name = models.CharField(max_length=255)
    gif_file = models.ImageField(upload_to='generated_gifs/')
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.FloatField()
    end_time = models.FloatField()