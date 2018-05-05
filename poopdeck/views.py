from django.shortcuts import render
from django.shortcuts import loader
from .models import Events
from .models import Cgr
from .models import Services
from .models import Meals
from .models import Day
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
from .forms import eventForm


# Create your views here.


def index(request):
	#return HttpResponse("Hello, world. You're at the end of the line honey")
	day = Day.objects.get(CalenderDate = datetime.date.today())
	events = day.events_set.all() #Grab all events from database
	meals = day.meals_set.all()
	cgr = day.cgr_set.all()
	context = {'events': events, 'day':day, 'meals': meals, 'cgr':cgr} #Fill a context with the events list
	template = loader.get_template('poopdeck/index.html')
	return HttpResponse(template.render(context, request))

def detail(request, event_id):
	try:
		event = Events.objects.get(pk=event_id)
		context = {'event':event}
	except Events.DoesNotExist:
		raise Http404("Event does not exist")
	return render(request, 'poopdeck/details.html', context)

def update(request, Events__IDNumber):
	new_IDNumber = request.POST['IDnumber']
	new_Description = request.POST['descirption']
	event = Events.objects.get(pk=Events_IDNumber)
	event.IDNumber = new_IDNumber
	event.Description = new_Description
	event.save()
	context = {'event':event}
	return render(request, 'poopdeck/details.html', context)

def addevent(request):
	if request.method == 'POST':
		form = eventForm(request.POST)
		if form.is_valid():
			newevent = form.save()
		return HttpResponseRedirect('/')
	else:
		form = eventForm()
	return render(request, 'poopdeck/add.html', {'form': form})


#from .forms import EventForm

#def event(request):
#	form = eventForm(request.POST or None)
#	if form.is_valid():
#		receiverInfo = eventForm(description = forms.cleaned_data['description'], duration = forms.cleaned_data['duration'], importance = forms.cleaned_data['importance'], location = forms.cleaned_data['location'], completionStatus = forms.cleaned_data['completion status'],)
#		receiverInfo.save()
#	return render(request, 'poopdeck/events.html', {'form': form})
