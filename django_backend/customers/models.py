from django.db import models

# Create your models here.


class Customers(models.Model):
	"""Customer data."""

	name = models.CharField(max_length=30)
	age  = models.IntegerField(null=True)
	is_active = models.BooleanField(default=True)