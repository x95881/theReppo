from django.urls import path, include
from . import views
from django.conf.urls import url


app_name='poopdeck'

urlpatterns = [
	path('', views.index, name='index'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('event/<int:event_id>/', views.detail, name='detail'),
	path('event/<int:event_id>/update', views.update, name='update'),	
	path('add', views.addevent, name='addevent'),
	path('details', views.detail, name='detail'),
	path('cgr/<int:cgr_id>/', views.cgr, name='cgr'),
	path('meal/<int:meal_id>/', views.meal, name='meal'),
	#path('<int:cgr_id>/', views.cgr, name='cgr'),
	#path('<int:cgr_id>/update', views.update, name='update'),
]

