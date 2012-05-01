from forms import *
from models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext

image_dir = "/Users/daniel/prog/arthome/media/"

def upload_art (request):
    if request.POST:
	try:
	   form = ArtworkForm(request.POST, request.FILES)
	   form.save()	
	except ValueError:
	    c = {}
	    c.update(csrf(request))
	    return render_to_response('add_artwork.html',{'form':form}, context_instance = RequestContext(request))
	    
	return HttpResponse('Done!')
    else:
	form = ArtworkForm()
	c = {}
	c.update(csrf(request))
	return render_to_response('add_artwork.html',{'form':form}, context_instance = RequestContext(request))
