from django.db import models

# Create your models here.
from django.db import models

class Events(models.Model):
	IDnumber = models.IntegerField()
	Description = models.CharField(max_length=100)
	DurationRange = models.CharField(max_length=30)
	ImportanceStatus = models.CharField(max_length=30)
	Location = models.CharField(max_length=30)
	CompletionStatus = models.CharField(max_length=3)
	#Yes or No
	def __str__(self):
		return self.IDnumber + "," + self.Description + "," + self.DurationRange + "," + self.ImportanceStatus + "," + self.Location + "," + self.CompletionStatus


class Meals(models.Model):
	MealID = models.IntegerField()
        TypeofMeal = models.CharField(max_length=20)
        SpecialOccasion = models.CharField(max_length=30)
	Location = models.CharField(max_length=30)
	DurationRange = models.CharField(max_length=30)
	AnnouncementsMade = models.CharField(max_length=200)
	def __str__(self):
		return self.MealID + "," + self.TypeofMeal + "," + self.SpecialOccasion + "," + self.Location + "," + self.DurationRange + "," + self.AnnouncementsMade
	

class Services(models.Model):
	IDNumber = models.IntegerField()
	Description = models.CharField(max_length=100)
	DurationRange = models.CharField(max_length=30)
	Location = models.CharField(max_length=30)
	Status = models.CharField(max_length=30)
	def __str__(self):
		return self.IDNumber + "," + self.Description + "," + self.DurationRange + "," + self.Location + "," + self.Status

class Cgr(models.Model):
	IDnumber = models.IntegerField()
	Company = models.CharField(max_length=100)
	DurationRange = models.CharField(max_legnth=30)
	DutyDriver = models.CharField(max_length=30)
	SergeantOfGuard = models.CharField(max_length=30)
	def __str__(self):
		return self.IDnumber + "," + self.Company + "," + self.DurationRange + "," + self.DutyDriver + "," + self.SergeantOfGuard
