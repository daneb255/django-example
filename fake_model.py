import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fomtest.settings')

import django
django.setup()

import random
from faker import Faker
from myfirstapp.models import Topic, Webpage, AccessRecord, User

fakegenerator = Faker()

topics = ['Search', 'Social', 'Shop', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        topic = add_topic()
        url = fakegenerator.url()
        date = fakegenerator.date()
        name = fakegenerator.company()

        webpage = Webpage.objects.get_or_create(topic_id=topic, url=url, name=name)[0]
        ar = AccessRecord.objects.get_or_create(access_at=date, webpage_id=webpage)


def populate_users(n=5):
    for entry in range(n):
        fake_name = fakegenerator.name().split()
        first_name = fake_name[0]
        last_name = fake_name[1]
        email = fakegenerator.email()

        User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)


if __name__ == '__main__':
    print("Generate data..")
    populate(20)
    populate_users(20)
    print("Generate data finished....")

