from django.contrib import admin
from .models import Events
from .models import Cgr
from .models import Services
from .models import Meals
from .models import Day
# Register your models here.

admin.site.register(Events)
admin.site.register(Cgr)
admin.site.register(Services)
admin.site.register(Meals)
admin.site.register(Day)
