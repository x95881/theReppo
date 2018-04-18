from django.urls import path, include
from . import views
from django.conf.urls import url


app_name='poopdeck'

urlpatterns = [
	path('', views.index, name='index'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('<int:event_id>/', views.detail, name='detail'),
	path('<int:event_id>/update', views.update, name='update'),	
	path('add', views.addevent, name='addevent'),
	path('details', views.detail, name='detail'),
	#path('<int:cgr_id>/', views.cgr, name='cgr'),
	#path('<int:cgr_id>/update', views.update, name='update'),
]

