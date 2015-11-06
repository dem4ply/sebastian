from django.db import models

# Create your models here.

class Document( models.Model ):
	key = models.CharField( max_length=5 )
	name = models.CharField( max_length=128 )
