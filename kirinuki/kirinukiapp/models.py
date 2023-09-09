import os
from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

# FileField
class FileUpload(models.Model):
    attach = models.FileField(
        upload_to='media/',
        verbose_name='添付ファイル',
        validators=[FileExtensionValidator(['mp3','avi' ])],
    )

    def __str__(self) -> str:
        return self.attach.name
