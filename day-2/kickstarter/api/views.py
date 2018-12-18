from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from api.models import Campaign
from django.core import serializers

def index(request):
  return HttpResponse("Hello, world. You're at the kicks index.")

def get_campaign(request, campaign_id):
  campaign = Campaign.objects.filter(id = campaign_id)
  response_value = serializers.serialize('json', campaign)
  return HttpResponse(response_value)
