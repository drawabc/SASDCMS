from django.db import models
import pytz, datetime
# Create your models here.

tz = pytz.timezone('Asia/Singapore')

class Report(models.Model):
    ASSISTANCE_TYPE_CHOICES = (
        ('EA', 'Emergency Ambulance'),
        ('RE', 'Rescue and Evacuation'),
        ('FF', 'Fire-fighting'),
        ('GL', 'Gas Leak Control'),
    )
    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=8)
    location = models.CharField(max_length=500)
    unit_number = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=6)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=2, choices=ASSISTANCE_TYPE_CHOICES)
    time = models.DateTimeField(default=datetime.datetime.now(tz=tz))

    def __str__(self):
        return "Report " + str(self.pk) + " at " + str(self.time.astimezone(tz))


class CivilianData(models.Model):
    nric = models.CharField(max_length=9)
    name = models.CharField(max_length=120)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    mobile = models.CharField(max_length=8)
    email = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk) + ". " + str(self.name) + str(self.nric)
