from django.urls import path
from django.shortcuts import redirect
from django.utils.dateparse import parse_date
from photos.models import PhotoComment
from photos import views

urlpatterns = [
  path('', views.index, {}),
  path('<int:photo_id>', views.photo_by_id, {}),
  path('date-picker', views.date_picker, {}),
  path('dates/<str:date>', views.photo_by_date, {})
]
