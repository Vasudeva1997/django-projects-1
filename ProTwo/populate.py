import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker()

topics = ['Search','Social','Marketplace','News','Games']

def addTopic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
    
def populate(N=5):
    for entry in range(N):
        top = addTopic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage = Webpage.objects.get_or_create(topic= top, url=fake_url,name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpage,date=fake_date)[0]

if __name__ == "__main__":
    print("Populating Script")
    populate(12)
    print("populated Script")