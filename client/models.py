from django.db import models

class Client( models.Model ):
	first_name = models.CharField( max_length=128 )
	last_name = models.CharField( max_length=128 )
