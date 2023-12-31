from django.db import models

# Create your models here.
class Blog(models.Model):
	id = models.AutoField(primary_key=True)
	title=models.CharField(max_length=255)
	pub_date= models.DateTimeField()
	body= models.TextField()
	img= models.ImageField(upload_to='images/')


	def summary(self):
		return self.body[:50]

	def pub_date1(self):
		return self.pub_date.strftime('%b %e, %Y')

	def __str__(self):
		return self.title  #for getting titles in admin pg