from django.db import models

class Profile(models.Model):
	username = models.CharField(max_length=50)
	orgName = models.CharField(max_length=30)
	rescueHome = models.CharField(max_length=30)
	bedsno = models.CharField(max_length=4, default = "100")
	contact = models.CharField(max_length=13)
	lattitude = models.CharField(max_length=30)
	longitude = models.CharField(max_length=30)

	def __str__(self):
		return self.username

class Coordinates(models.Model):
	lattitude = models.CharField(max_length=15)
	longitude = models.CharField(max_length=15)

	def __str__(self):
		return self.lattitude

class userData(models.Model):
	rescueHome = models.CharField(max_length=50, default="None")
	amenities = models.CharField(max_length=100, default="Nothing")
	waterlevel = models.CharField(max_length=10, default="Low")
	levelchange = models.CharField(max_length=10, default="Decreasing")
	feedback = models.CharField(max_length=500, default="No feedback")
	degree = models.FloatField(default=0)

	def __str__(self):
		return self.rescueHome

class userInfo(models.Model):
	username = models.CharField(max_length=50)
	name = models.CharField(max_length=40)
	email = models.CharField(max_length=254)
	contact = models.CharField(max_length=13)
	family = models.IntegerField()

	def __str__(self):
		return self.name

class rescueCenter(models.Model):
	username = models.CharField(max_length=50)
	lattitude = models.CharField(max_length=20)
	longitude = models.CharField(max_length=20)

	def __str__(self):
		return self.username