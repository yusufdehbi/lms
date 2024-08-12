from django.core.management.base import BaseCommand
from faker import Faker
from dashboard.models import Department
import random


class Command(BaseCommand):
    help = 'Seed the database with fake departmenet data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database with department ...')
        departments = [
            "Human Resources",
            "Finance",
            "Marketing",
            "Sales",
            "Research and Development",
            "Customer Service",
            "IT Support",
            "Legal",
            "Operations",
            "Product Management"
        ]
        for _ in range(6):
            random_department = random.choice(departments)
            self.stdout.write(self.style.SUCCESS(f'{random.choice(departments)} seeded !!'))
            Department.objects.create(
                name=random_department
            )
