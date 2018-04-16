from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('accounts/', include('django.contrib.auth.urls')),
	#path('<int:cgr_id>/', views.cgr, name='cgr'),
	#path('<int:cgr_id>/update', views.update, name='update'),
]

