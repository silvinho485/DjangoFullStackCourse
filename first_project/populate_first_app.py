import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

##FAKE POP SCRIPT

import random
from faker import Faker
from first_app.models import (AccesRecord,
Webpage,
Topic)

fakegen = Faker()
topics = ['Search', 'Social', 'MarketPlace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # Createthe fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.name()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #create an fake acces for that Webpage

        acc_rec  = AccesRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating complete!")
