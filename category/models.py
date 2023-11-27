from django.db import models
from baseapp.models import  BaseModel

import os
from django.core.exceptions import ValidationError


def validate_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.png', '.word', '.jpg', 'excel']
    if not ext.lower() in valid_extensions:
        raise ValidationError('You must enter .pdf, .png, .word, .jpg, .excel   file ')



class File(BaseModel):
      file_name = models.CharField(max_length=300, verbose_name="Fayl nomi:")
      file_type =  models.FileField(upload_to='audio/', verbose_name="Faylni tanlang", validators=[validate_file])
      size = models.CharField(max_length=200, verbose_name="fayl razmeri:")


      class Meta:
          verbose_name = "Fayl bolimi_"
