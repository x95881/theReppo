from django.test import TestCase

# Create your tests here.
def index(request):
        return HttpResponse("Hello, world. You're at the Reppo index.")

