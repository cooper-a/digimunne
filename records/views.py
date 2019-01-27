from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

#from .models import Vaccination
from .models import Patient
from .models import Vaccination


# Create your views here.
def index(request):
    #all_vaccinations = Vaccination.objects.all()
    all_patients = Patient.objects.all()
    all_vaccinations = Patient.objects.all()
    context = {
        'all_vaccinations': all_vaccinations,
        'all_patients': all_patients,
    }
    template = loader.get_template('records/index.html')
    return HttpResponse(template.render(context, request))

