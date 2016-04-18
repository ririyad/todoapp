from django.shortcuts import render
from .models import todo
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404

def index(request): #Define our function, accept a request
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    items = todo.objects.all() # ORM queries the database for all of the to-do entries.
    return render_to_response('index.html', {'items': items})