from django.db import models

# Create your models here.
from django.db import models

class Events(models.Model):
	Idnumber = models.IntegerField()
	Description = models.CharField(max_length=100)
	DurationRange = models.CharField(max_length=30)
	ImportanceStatus = models.CharField(max_length=30)
	Location = models.CharField(max_length=30)
	CompletionStatus = models.CharField(max_length=3)
	#Yes or No
	def __str__(self):
		return self.Idnumber + "," + self.Description + "," + self.DurationRange + "," + self.ImportanceStatus + "," + self.Location + "," + self.CompletionStatus


class Meals(models.Model):
        TypeofMeal = models.CharField(max_length=20)
        SpecialOccasion = models.CharField(max_length=30)
	Location = models.CharField(max_length=30)
	DurationRange = models.CharField(max_length=30)
	AnnouncementsMade = models.CharField(max_length=200)
	def __str__(self):
		return self.TypeofMeal + "," + self.SpecialOccasion + "," + self.Location + "," + self.DurationRange + "," + self.AnnouncementsMade
	

class Services(models.Model):
	IDNumber = models.CharField(max_length=5)
	Description = models.CharField(max_length=100)
	DurationRange = models.CharField(max_length=30)
	Location = models.CharField(max_length=30)
	Status = models.CharField(max_length=30)
	def __str__(self):
		return self.Description + "," + self.DurationRange + "," + self.Location + "," + self.Status
