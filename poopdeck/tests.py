from django.test import TestCase
from poopdeck.models import *

# Create your tests here.
def index(request):
        return HttpResponse("Hello, world. You're at the Reppo index.")

#####################################################

class EventsTestCase(TestCase):
        def setUp(self):
                Events.objects.create(
                        IDnumber = 100001,
                        Description = "test test test",
                        DurationRange = "100001",
                        ImportanceStatus = "100001",
                        Location = "test location",
                        CompletionStatus = "testing Testing" 
                )
        def test_event_was_made(self):
                # checks if data can be retreived 
                test_event = Events.objects.get(IDnumber = 100001)
                test_event

            
        
class MealsTestCase(TestCase):
        def setUp(self):
                Meals.objects.create(
                        MealID = 100001,
                        TypeofMeal = "test meal",
                        SpecialOccasion = "test special occ",
                        Location = "test LOC",
                        DurationRange = "test dur",
                        AnnouncementsMade = "Test Annonce"
                )
        def test_meal_was_made(self):
                # checks if data can be retreived 
                test_meal = Meals.objects.get(IDnumber = 100001)
                test_meal
                
                
class ServicesTestCase(TestCase):
        def setUp(self):
                Services.objects.create(
                        IDNumber = 1000001,
                        Description = "test descr",
                        DurationRange = " test Dur Range",
                        Location = " test location",
                        Status = "test status"
                )
        def test_service_was_made(self):
                # checks if data can be retreived 
                test_Service = Services.objects.get(IDnumber = 1000001)
                test_Service
                
                
                
                
class CgrTestCase(TestCase):
        def setUp(self):
                Cgr.objects.create(
                        IDNumber = 1000001,
                        Company = "J5"
                        DurationRange = " test Dur Range",
                        DutyDriver = models.CharField(max_length=30)
                        SergeantOfGuard = models.CharField(max_length=30)
                )
        def test_Cgr_was_made(self):
                # checks if data can be retreived 
                test_Cgr = Cgr.objects.get(IDnumber = 1000001)
                test_Cgr
                
               
        
class DayTestCase(TestCase):
        def setUp(self):
                Day.objects.create()
        def test_Day_was_made(self):
                # checks if data can be retreived 
                test_Day = Day.objects.get()
                test_Day
                
class ConnectDayTestCase(TestCase):
        def setUp(self):
                ConnectDay.objects.create()
        def test_connect_day(self):
                test_connect = ConnectDay.objects.get()
                
