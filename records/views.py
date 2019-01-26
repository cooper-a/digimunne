from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Question
from .models import Choice

# Create your views here.
def index(request):
    all_questions = Question.objects.all()
    context = {
        'all_questions': all_questions,
    }
    template = loader.get_template('records/index.html')
    return HttpResponse(template.render(context, request))

