from django.http import HttpResponse

def homepage(reguest):
  return HttpResponse("Hello")