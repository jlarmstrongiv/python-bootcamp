from django.shortcuts import render
from django.http import HttpResponse
from photos.models import PhotoComment
from django.shortcuts import redirect
import requests
import time
from datetime import datetime, timedelta

api_key = "oMrH77hL0IcYFpEAYw6HpzxULiro2VX2jGy9CIMV"

# Create your views here.
def index(request):
  if (request.method == 'GET'):
    comments = PhotoComment.objects.all()
    return render(request, 'photos.html', {'comments': comments})
  return HttpResponse('Invalid Method')

def photo_by_id(request, photo_id):
  if (request.method == 'GET'):
    photo_comment = PhotoComment.objects.get(id=photo_id)
    return render(request, 'photo.html', {'photo_comment': photo_comment})
  return HttpResponse('Invalid Method')
# 24 March
def photo_by_date(request, date):
  if (request.method == 'GET'):
    r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}')
    photo_url = r.json()['url']
    print(photo_url)
    return render(request, 'date-photo.html', {'photo_url': photo_url, 'photo_date': date})
  if (request.method == 'POST'):
    photo_comment = PhotoComment.objects.create(
      comment=request.POST.get('comment'),
      rating=request.POST.get('rating'),
      date=date,
      url=request.POST.get('url')
    )
    return redirect(f'/photos/{photo_comment.id}')
  return HttpResponse('Invalid Method')

def date_picker(request):
  if (request.method == 'GET'):
    date = datetime.now()
    day = f'{date:%d}'
    month = f'{date:%m}'
    year = f'{date:%Y}'
    request_date = f'{year}-{month}-{day}'
    return render(request, 'date-picker.html', {'today': request_date})
    # return HttpResponse('date')
  if (request.method == 'POST'):
    date = request.POST.get('date')
    return redirect(f'/photos/dates/{date}')
  return HttpResponse('Invalid Method')
