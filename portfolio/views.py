from django.shortcuts import render
from .models import Project
from .models import Person
# Create your views here.
def home(request):
    projects= Project.objects.all()
    person= Person.objects.all()
    global context
    context= {
        'projects': projects,
        'person':person
    }
    return render(request, 'portfolio/home.html',context=context )
def base(request):
	return render(request,'portfolio/base.html',context=context)
def log(request):
	return render(request,'portfolio/login.html')