from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from .models import photos
# from .models import Image

admin.site.register(photos)
# admin.site.register(Image)