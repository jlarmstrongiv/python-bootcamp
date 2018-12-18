import csv
from django.core.management import BaseCommand
from datetime import datetime
from django.utils import timezone
from api.models import Campaign
# ./manage.py load_data --path /Users/jlarmst/Desktop/react/python/bootcamp/day-2/kickstarter/api/Kickstarter.csv
# ./manage.py makemigrations
# ./manage.py migrate
# python manage.py runserver
class Command(BaseCommand):
  def add_arguments(self, parser):
    parser.add_argument('--path', type=str)

  def handle(self, *args, **kwargs):
    path = kwargs['path']
    with open(path) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count=0
      for row in csv_reader:
        if (line_count is not 0):
          Campaign.objects.create(
            backers_count = row[0],
            blurb = row[1],
            category = row[2],
            converted_pledged_amount = row[3],
            country = row[4],
            created_at = datetime.fromtimestamp(int(row[5]), timezone.utc),
            creator = row[6],
            currency = row[7],
            deadline = datetime.fromtimestamp(int(row[8]), timezone.utc),
            disable_communication = row[9].capitalize(),
            fx_rate = row[10],
            goal = row[11],
            kick_id = row[12],
            launched_at = datetime.fromtimestamp(int(row[13]), timezone.utc),
            location = row[14],
            name = row[15],
            photo = row[16],
            pledged = row[17],
            profile = row[18],
            slug = row[19],
            source_url = row[20],
            spotlight = row[21].capitalize(),
            staff_pick = row[22].capitalize(),
            state = row[23],
            state_changed_at = datetime.fromtimestamp(int(row[24]), timezone.utc),
            static_usd_rate = row[25],
            urls = row[26],
            usd_pledged = row[27],
            usd_type = row[28]
          )
        line_count =+ 1
    print('Sanity Check')
