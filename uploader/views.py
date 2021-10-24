import os
import requests
from django.shortcuts import render
from .forms import ImageForm
from .models import photos
# from .templates import templates
# Create your views here.

# from django.conf import settings
# ImageForm._size > settings.MAX_UPLOAD_SIZE

def home(request):
  if request.method == "POST":
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
  form = ImageForm()
  img = photos.objects.all()
  a = []
  for i in img:
   a.append(len(requests.get(i.image.url).content))
  print(a)
  print(img)
  return render(request, 'home.html', {'img':img, 'form':form, 'a': a})

 