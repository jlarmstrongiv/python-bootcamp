from django.db import models

# Create your models here.
class Campaign(models.Model):
  backers_count = models.IntegerField()
  blurb = models.TextField()
  category = models.TextField() # DictWrapper
  converted_pledged_amount = models.IntegerField()
  country = models.TextField()
  created_at = models.TimeField()
  creator = models.TextField() # DictWrapper
  currency = models.TextField()
  deadline = models.TimeField()
  disable_communication = models.BooleanField()
  fx_rate = models.FloatField()
  goal = models.FloatField()
  kick_id = models.IntegerField()
  launched_at = models.TimeField()
  location = models.TextField() # DictWrapper
  name = models.TextField()
  photo = models.TextField() # DictWrapper
  pledged = models.FloatField()
  profile = models.TextField() # DictWrapper
  slug = models.TextField()
  source_url = models.URLField()
  spotlight = models.BooleanField()
  staff_pick = models.BooleanField()
  state = models.TextField()
  state_changed_at = models.TimeField()
  static_usd_rate = models.FloatField()
  urls = models.TextField() # DictWrapper
  usd_pledged = models.FloatField()
  usd_type = models.TextField()
