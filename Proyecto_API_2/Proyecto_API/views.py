

from django.http import HttpResponse

# Request: Para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP

def welcome(request):
    return HttpResponse("Hello to this course of Django. =)")