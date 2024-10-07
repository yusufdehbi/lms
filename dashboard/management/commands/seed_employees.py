import random

from django.core.management.base import BaseCommand
from faker import Faker
from dashboard.models import User, Employee, Position, Department


class Command(BaseCommand):
    help = 'Seed the database with fake employees data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        self.stdout.write('Seed database with employees data...')
        positions = Position.objects.all()
        department = Department.objects.all()
        genders = [User.MALE, User.FEMALE]
        for index in range(10):
            user = User.objects.create(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                gender=random.choice(genders),
            )
            Employee.objects.create(
                user=user,
                position=random.choice(positions),
                department=random.choice(department),
                date_joined=fake.past_date(),
                employee_id=fake.uuid4().replace('-', '')[:8]
            )
            self.stdout.write(self.style.SUCCESS(f'Employee {index} / 10 inserted !!'))
