from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from AppTwo.models import WebUsers, Topic #Importing the models of AppTwo
from AppTwo.forms import NewUserForm
from django.urls import reverse

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

def forms(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse("AppTwo:users")) #view called at the end
        else:
            print("ERROR!")
            print(form.errors)
    return render(request, 'AppTwo/forms.html', {'form':form})
