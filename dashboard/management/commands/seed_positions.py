from django.core.management.base import BaseCommand
from faker import Faker
from dashboard.models import Position


class Command(BaseCommand):
    help = 'Seed the database with fake job positions data'

    def handle(self, *args, **options):
        fake = Faker()
        self.stdout.write('Seeding database with job positions ...')
        for _ in range(10):
            fake_job = fake.job()
            positions = Position.objects.create(
                name=fake_job
            )
            self.stdout.write(self.style.SUCCESS(f'{fake_job} seeded !!'))

