import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','assignment.settings')

import django
django.setup()

import random
from user_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5,first_name=fakegen.name().split()[0],last_name=fakegen.name().split()[1],email=fakegen.email()):
    for i in range(N):
        u = User(first_name =first_name, last_name = last_name, email=email)
        u.save()

if __name__ == "__main__":
    print("Populating.........")
    populate(12)
    print("Populated....!!")