import os
os. environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_prework_base.settings')

import django
django.setup()

import random
from prework_app.models import Users
from faker import Faker

fakegen = Faker()

def pop_users(N=5):
    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        users = Users.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)


if __name__ == '__main__':
    print("Populating User data")
    pop_users(20)
    print("Users Created")
