from django.db import models

class Unit_of_measure( models.Model ):
	key = models.CharField( max_length=16 )
	name = models.CharField( max_length=128 )

class Article( models.Model ):
	sku = models.CharField( max_length=20 )
	upc = models.CharField( max_length=13 )
	number_part = models.CharField( max_length=20 )
	name = models.CharField( max_length=128 )

	unit_of_measure = models.ForeignKey( Unit_of_measure )

class Warehouse( models.Model ):
	name = models.CharField( max_length=128 )

class Warehouses_existence( models.Model ):
	article = models.ForeignKey( Article )
	warehouse = models.ForeignKey( Warehouse )
