from django.db import models

# Create your models here.
class faculty(models.Model):
	fid=models.IntegerField()
	fname=models.CharField(max_length=30)
	fmail=models.EmailField()
	fpass=models.CharField()
	

