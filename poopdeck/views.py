from django.shortcuts import render
from django.http import HttpResponse
from .models import Events
from django.template import loader
from  .forms import eventForm


# Create your views here.
def index(request):
	#return HttpResponse("Hello, world. You're at the end of the line honey")
	events = Events.objects.all() #Grab all events from database
	context = {'events': events} #Fill a context with the events list
	template = loader.get_template('poopdeck/index.html')
	return HttpResponse(template.render(context, request))






def event(request):
	form = eventForm(request.POST or None)
	if form.is_valid():
		receiverInfo = eventForm(description = forms.cleaned_data['description'], duration = forms.cleaned_data['duration'], importance = forms.cleaned_data['importance'], location = forms.cleaned_data['location'], completionStatus = forms.cleaned_data['completion status'],)
		receiverInfo.save()
	return render(request, {'form': form})
