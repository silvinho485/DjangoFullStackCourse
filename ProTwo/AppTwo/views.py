from django.shortcuts import render
from django.http import HttpResponse

def help(request):
    my_dict = {
        "dict_call":"Dictionary result",
    }

    return render(request, "AppTwo/help.html", context=my_dict)

# Create your views here.
