from django.db import models

class Artwork(models.Model):
    title = models.CharField(max_length=50)
    artist_name = models.CharField(max_length=50)
    artist_website = models.URLField(blank = True)
    description = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='images/')
    default_price = models.DecimalField(max_digits=8, decimal_places=2)
    #pieces = models.ManyToManyField('ArtworkPiece')

    def __unicode__(self):
        return self.title

class ArtworkPiece(models.Model):
    artwork = models.ForeignKey('Artwork')
    price = models.DecimalField(max_digits=8, decimal_places=2)		# funding required
    
    def __unicode__(self):
	return '[%d] %s' % (self.id, self.artwork.title)

class Donor(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    #fundings = models.ManyToManyField('Funding')
	
    def __unicode__(self):
	return self.email

class Funding(models.Model):
    piece = models.ForeignKey(ArtworkPiece)
    donor = models.ForeignKey(Donor, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date_time = models.DateTimeField(blank=True)

    def __unicode__(self):
	return self.piece
