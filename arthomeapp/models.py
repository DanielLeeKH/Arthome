from django.db import models

class Artwork(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='images/')

    def __unicode__(self):
        return self.title

    def get_image_filename():
	return 'img%s,jpg' % str(id).rjust(5,'0')

	

