from django.shortcuts import render
from django.http import HttpResponse
from.models import Question
from.models import Choice
def home(request):
    post=Question.objects.all()
    return render(request,'testapp/home.html',{'post':post})

def choice(request):
    post=Choice.objects.all()
    return render(request,'testapp/django.html',{'post':post})

def index(request):
    return render(request,'testapp/index.html',{'name':'Ashok'})


from django.shortcuts import render
from .forms import StudentForm

def forms(request):
    student = StudentForm()
    return render(request, 'testapp/forms.html', {'form': student})