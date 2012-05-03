from forms import *
from models import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from datetime import datetime

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
	return render_to_response('add_artwork.html', {'form':form}, context_instance = RequestContext(request))


def gallery(request):
    artworks = Artwork.objects.all()
    return render_to_response('gallery.html', {'artworks':artworks}, context_instance=RequestContext(request))


def view_artwork(request, artwork_id):
    artwork = Artwork.objects.get(id=artwork_id)
    artwork_pieces = artwork.artworkpiece_set.all()
    
    # find out funding info per art piece
    funding_info = []
    for artwork_piece in artwork_pieces:
	# calculate total funds raised so far
	amount = 0
	for funding in artwork_piece.funding_set.all():
	    amount = amount + funding.amount
	funding_info.append((artwork_piece.id, amount, artwork_piece.price))
    return render_to_response('view_artwork.html', {'artwork':artwork, 'funding_info':funding_info}, context_instance=RequestContext(request))

	
def fund_artwork(request, artwork_id):
    if request.POST:
	funding_amount = int(request.POST['amount'])
	artwork = Artwork.objects.get(id=request.POST['artwork_id'])
        artwork_pieces = artwork.artworkpiece_set.all()
	
	for artwork_piece in artwork_pieces:
	    # calculate total funds raised so far
	    total_amount = 0
	    for funding in artwork_piece.funding_set.all():
		total_amount = total_amount + funding.amount
	    # fund the first incompletely funded piece
	    if total_amount < artwork_piece.price:
		funding = Funding(piece=artwork_piece, amount=funding_amount, donor=Donor.objects.get(id=1), date_time=datetime.now())
		funding.save()
		break

	return HttpResponseRedirect('/view_artwork/%s' % artwork_id)
    else:
        return render_to_response('fund_artwork.html', {'artwork_id':artwork_id}, context_instance=RequestContext(request))


def login(request):
    if request.POST:
	username = request.POST['username']
	password = request.POST['password']
	try:
	    user = Donor.objects.get(email__exact=username)
	    if password == user.password:
		result = 'OK'
		request.session['user'] = user
	    else:
		result = 'Fail'
	except ObjectDoesNotExist:
	    result = 'User not found'
	    
	return HttpResponse(result)
    else:
	form = LoginForm()
	return render_to_response('login.html',{'form':form}, context_instance = RequestContext(request))


