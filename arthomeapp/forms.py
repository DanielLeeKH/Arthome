from django.forms import ModelForm
from models import *

class ArtworkForm (ModelForm):
    class Meta:
	model = Artwork

