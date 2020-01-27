from django.db import models

# Create your models here.

class Admission(models.Model):
	

	GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown'),
    )
	admission_date = models.DateTimeField('date admissioned')
	name = models.CharField(max_length=30)
	bed_number = models.CharField(max_length=30)
	chart_id = models.CharField(max_length=30 )
	age = models.PositiveSmallIntegerField(blank=True,null=True)
	sex = models.CharField(max_length=1, choices = GENDER,blank=True)
	diagnosis = models.CharField(max_length=100,blank=True)
	secondary_diagnosis =  models.CharField(max_length=100,blank=True)
	progress_note = models.TextField(blank=True)
	admission_note = models.TextField(blank=True)
	discharge_note =  models.TextField(blank=True)
	weekly_summary =  models.TextField(blank=True)
	discharged = models.BooleanField()
	memo = models.TextField(blank=True)

	def __str__(self):
		return "{} - {}".format(self.bed_number, self.name)



class Item(models.Model):
	admission = models.ForeignKey(Admission,on_delete = models.CASCADE)
	content = models.CharField(max_length=255)
	start_time = models.DateTimeField(blank=True,null=True)
	stop_time = models.DateTimeField(blank=True,null=True)
	alert_time = models.DateTimeField(blank=True,null=True) 
	done =   models.BooleanField()
	priority = models.PositiveSmallIntegerField(blank=True,null=True)
	color = models.CharField(max_length=30,blank=True)

	def __str__(self):
		return "{} - {}".format(self.content, self.admission.name)
