# Generated by Django 2.1.4 on 2018-12-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='goal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='pledged',
            field=models.FloatField(),
        ),
    ]