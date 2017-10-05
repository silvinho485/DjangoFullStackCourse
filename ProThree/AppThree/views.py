from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to AppThree Index!")

def otherFunc(request):
    other_dict = {
        'other_key':'Other dictionary thing',
    }
    return render(request, 'AppThree/other.html', context=other_dict)
# Create your views here.
