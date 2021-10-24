from django.core import validators
from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from .validators import validate_file_size
import datetime



# Create your models here.
# class Image(models.Model):
#  photo = models.ImageField(upload_to="myimage")



# from django.db import models
from cloudinary.models import CloudinaryField

class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image', validators=[validate_file_size])
    date = models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.title
    @property
    def filesize(self):
        x = self.image.size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return self.str(value)+ext


    # validators = [FileExtensionValidator(['png','jpeg'])