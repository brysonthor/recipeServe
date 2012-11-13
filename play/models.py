from django.db import models

class users(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=64) #sha256 length
	creationDate = models.DateTimeField(auto_now_add='TRUE')
	def __unicode__(self):
		return u"%s %s" % (self.username, self.creationDate)


class ingredient(models.Model):
	name = models.CharField(max_length=50)
	def __unicode__(self):
		return u"%s" % self.name
	class Meta:
		ordering = ('name',)

class recipe(models.Model):
	name = models.CharField(max_length=50)
	ingredients = models.ManyToManyField(ingredient)
	def __unicode__(self):
		return u"%s" % self.name
	class Meta:
		ordering = ('name',)



# Create your models here.
