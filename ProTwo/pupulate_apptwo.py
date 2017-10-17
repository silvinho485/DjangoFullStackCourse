import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings') #import from setting

import django
django.setup()

##FAKE POP SCRIPT

import random
from faker import Faker
from AppTwo.models import (Topic,
WebUsers) #What you want to populate


fakegen = Faker() #Fake generator created
topics = ['Food', 'travels', 'TV'] #just an example of topics, you can put anything you want here

def add_topic():
    """
    Function to add create a new topic and save it
    """
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    """
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    This return two parameters the firs is the object, and second is an boolean
    True if is new, os False if exist
    """
    t.save() #save it
    return t

def populate(N=5):

    for entry in range (N):

        top = add_topic()

        fake_name = fakegen.name()
        fake_lname = fakegen.last_name()
        fake_mail = fakegen.email()

        #created variables to contain the population

        webusr = WebUsers.objects.get_or_create(
        topic=top,
        name=fake_name,
        lname=fake_lname,
        email=fake_mail)

        #variables has been passed to models


        if __name__ == '__main__':
            print("Populating models")
            populate(18)
            print("Models pupulated")
