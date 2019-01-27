from django.db import models

# Create your models here.
class Patient(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    year_ob = models.CharField(max_length=4)
    month_ob = models.CharField(max_length=2)
    day_ob = models.CharField(max_length=2)

    def __str__(self):
        return self.first_name + " " + self.last_name
    


class Vaccination(models.Model):
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    disease_name = models.CharField(max_length=200)
    patient = models.ManyToManyField(Patient)

    def __str__(self):
        return self.disease_name

    #patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    

