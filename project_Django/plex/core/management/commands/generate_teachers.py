import random

from core.models import Teacher

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    _help = 'Generate list of 100 teachers'

    def handle(self, *args, **options):
        fake = Faker("ru_Ru")
        data_set = []
        while len(data_set) != 100:
            gender = 'M' if random.randint(0, 1) == 0 else 'F'
            name = fake.first_name_male() \
                if gender == 'M' else fake.first_name_female()
            middle_name = fake.middle_name_male() \
                if gender == 'M' else fake.middle_name_female()
            surname = fake.last_name_male() \
                if gender == 'M' else fake.last_name_female()
            age = random.randint(22, 60)

            data = [surname, name, surname]
            if data in data_set:
                continue

            save_data = Teacher(last_name=surname, first_name=name,
                                middle_name=middle_name, age=age)

            save_data.save()
            data_set.append(data)
