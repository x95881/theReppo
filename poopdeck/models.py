# Create your models here.
from django.db import models
from django.utils import timezone

class Day(models.Model):
	#CalenderDate = models.CharField(max_length=100)
	CalenderDate = models.DateField()
	#Meal = models.ForeignKey(Meals, on_delete=models.CASCADE)
	#Events = models.ForeignKey(Events, on_delete=models.CASCADE)
	#CGREventID = models.ForeignKey(Cgr, on_delete=models.CASCADE)
	#ServicesID = models.IntegerField()
	Weather = models.CharField(max_length=50)
	Uniform = models.CharField(max_length=20)
	TAPS = models.IntegerField()
	DescriptionOfDay = models.CharField(max_length=30)
	def __str__(self):
		return str(self.CalenderDate) +  ","  + self.Weather + "," + self.Uniform + "," + str(self.TAPS) + "," + self.DescriptionOfDay

class Events(models.Model):
	Day = models.ForeignKey(Day, on_delete=models.CASCADE, default=1)
	Description = models.CharField(max_length=100)
	DurationRange = models.CharField(max_length=30)
	ImportanceStatus = models.CharField(max_length=30)
	Location = models.CharField(max_length=30)
	CompletionStatus = models.CharField(max_length=3)
	#Yes or No
	def __str__(self):
		return self.Description + "," + self.DurationRange + "," + self.ImportanceStatus + "," + self.Location + "," + self.CompletionStatus

#class Meals(models.Model):
#	Day = models.ForeignKey(Day, on_delete=models.CASCADE)
#	TypeofMeal = models.CharField(max_length=20)
#	SpecialOccasion = models.CharField(max_length=30)
#	Location = models.CharField(max_length=30)
#	DurationRange = models.CharField(max_length=30)
#	AnnouncementsMade = models.CharField(max_length=200)
#	def __str__(self):
#		return self.MealID + "," + self.TypeofMeal + "," + self.SpecialOccasion + "," + self.Location + "," + self.DurationRange + "," + self.AnnouncementsMade

class Meals(models.Model):
        Day = models.ForeignKey(Day, on_delete=models.CASCADE, default=1)
        TypeofMeal = models.CharField(max_length=20)
        SpecialOccasion = models.CharField(max_length=30)
        Location = models.CharField(max_length=30)
        DurationRange = models.CharField(max_length=30)
        AnnouncementsMade = models.CharField(max_length=200)
        def __str__(self):
                return  self.TypeofMeal + "," + self.SpecialOccasion + "," + self.Location + "," + self.DurationRange + "," + self.AnnouncementsMade


class Cgr(models.Model):
	Day = models.ForeignKey(Day, on_delete=models.CASCADE, default=1)
	Company = models.CharField(max_length=100)
	DurationRange = models.CharField(max_length=30)
	DutyDriver = models.CharField(max_length=30)
	SergeantOfGuard = models.CharField(max_length=30)
	def __str__(self):
		return  self.Company + "," + self.DurationRange + "," + self.DutyDriver + "," + self.SergeantOfGuard

class Services(models.Model):
	Description = models.CharField(max_length=100)
	DurationRange = models.CharField(max_length=30)
	Location = models.CharField(max_length=30)
	Status = models.CharField(max_length=30)
	def __str__(self):
		return  self.Description + "," + self.DurationRange + "," + self.Location + "," + self.Status

#class ConnectDay(models.Model):
#	CallID = models.ForeignKey(Day, on_delete=models.CASCADE)
#	IDnumber = models.ForeignKey(Services, on_delete=models.CASCADE)
#	def __str__(self):
#		return self.CallID + "," + self.IDnumber
    
class ConnectDay(models.Model):
        Call = models.ForeignKey(Day, on_delete=models.CASCADE)
        IDnumber = models.ForeignKey(Services, on_delete=models.CASCADE)
        def __str__(self):
                return self.Call + "," + self.IDnumber

