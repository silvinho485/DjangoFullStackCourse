from django.shortcuts import render
from django.http import HttpResponse
# from django.core.urlresolvers import reverse
from first_app.models import (AccesRecord,
                                    Topic,
                                    Webpage)

def index(request):
    webpages_list = AccesRecord.objects.order_by('date')
    exemplo1 = Webpage.objects.order_by('name')
    my_dict = {
        'insert_me':'Hello!I am from views.index!',
        'tester':'And I am a succesfull test :D',
        'help_url':reverse('help'),
        'exemplo1':exemplo1,
        'access_records':webpages_list,
    }
    return render(request, 'first_app/index.html', context=my_dict)

# Create your views here.
def help (request):
    help_dict = {"help_key":"Help_content"}
    return render(request, "first_app/help.html", context=help_dict)

def picture (request):
    # mdict = {
    #     "mkey":"Mresult"
    # }
    return render(request, "first_app/picture.html")
