from django.db import models

# Create your models here.
class Polls(models.Model):
	election_name=models.CharField(max_length=100)
	
	date_of_election=models.DateTimeField('elec_date')
	
	
class Choice(models.Model):
	candidate=models.CharField(max_length=50)
	
	cand_count=models.IntegerField(default=0)
	election_name=models.ForeignKey(Polls,on_delete=models.CASCADE)
	