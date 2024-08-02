from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    questions = Question.objects.all()

    context = {
        'questions':questions,
    }

    return render(request, 'index.html', context )