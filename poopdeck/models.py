from django.db import models

# Create your models here.
from django.db import models

class Events(models.Model):
	first = models.CharField(max_length=200)
	last = models.CharField(max_length=200)
	xnumber = models.CharField(max_length=8)
	def __str__(self):
		return self.last + "," + self.first


class Meals(models.Model):
        TypeofMeal = models.CharField(max_length=20)
        SpecialOccasion = models.CharField(max_length=30)
	Location = models.CharField(max_length=30)
	DurationRange = models.CharField(max_length=30)
	AnnouncementsMade = models.CharField(max_length=200)
	def __str__(self):
		return self.TypeofMeal + "," + self.SpecialOccasion + "," + self.Location + "," + self.DurationRange + "," + self.AnnouncementsMade
	
