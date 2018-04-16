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
                test_event = Event.objects.get(IDnumber = 100001)
                test_event
