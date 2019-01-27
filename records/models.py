from django.db import models

# Create your models here.

class Vaccination(models.Model):
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    disease_name = models.CharField(max_length=200)
    expiration_date = models.CharField(max_length=200)

    def __str__(self):
        return (self.disease_name + '\n\t' 
                + self.day + '-' + self.month + "-" + self.year)

    class Meta:
        ordering = ('disease_name',)

    pass
    

class Patient(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    year_of_birth = models.CharField(max_length=4)
    month_of_birth = models.CharField(max_length=2)
    day_of_birth = models.CharField(max_length=2)
    vaccinations = models.ManyToManyField(Vaccination)

    def __str__(self):
        return self.first_name + " " + self.last_name
