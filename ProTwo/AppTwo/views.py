from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import WebUsers, Topic

def index(request):
    return HttpResponse("You're in the app index")

def help(request):
    my_dict = {
        "dict_call":"Dictionary result",
    }
    return render(request, "AppTwo/help.html", context=my_dict)

def users(request):
    webusrs = WebUsers.objects.order_by('name')
    dicto = {
        "one_key":"One register",
        "webusrs":webusrs,
    }

    return render(request, 'AppTwo/users.html', context=dicto)
