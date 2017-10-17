from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import WebUsers, Topic #Importing the models of AppTwo

def index(request):
    return HttpResponse("You're in the app index")

def help(request):
    my_dict = {
        "dict_call":"Dictionary result",
    }
    return render(request, "AppTwo/help.html", context=my_dict)

def users(request):
    webusers = WebUsers.objects.order_by('name')
    topz = Topic.objects.order_by('top_name')
    dicto = {
        "one_key":"One register",
        "webusrs":webusers,
        "topicz":topz,
    }

    return render(request, 'AppTwo/users.html', context=dicto)
