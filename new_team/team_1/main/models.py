from django.db import models

class Links(models.Model):
	link = models.CharField("Link", max_length=500)

	def __str__(self):
		return self.link