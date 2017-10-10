import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

##FAKE POP SCRIPT

import random
from faker import Faker
from AppTwo.models import (Topic,
WebUsers)


fakegen = Faker()
topics = ['Food', 'travels', 'TV']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range (N):

        top = add_topic()

        fake_name = fakegen.name()
        fake_lname = fakegen.last_name()
        fake_mail = fakegen.email()

        webusr = WebUsers.objects.get_or_create(
        topic=top,
        name=fake_name,
        lname=fake_lname,
        email=fake_mail)


if __name__ == '__main__':
    print("Populating models")
    populate(18)
    print("Models pupulated")
