from django.core.management.base import BaseCommand
from dashboard.models import LeaveType


class Command(BaseCommand):
    help = 'Seed the database with fake employees data'

    def handle(self, *args, **kwargs):
        leave_types = [
            {"name": "Annual Leave", "description": "Paid leave accrued at 1.5 days per month after six months of service.", "days_allocated": 18, "gender_restriction": LeaveType.ANY},
            {"name": "Sick Leave", "description": "Paid sick leave after 54 days of contributions.", "days_allocated": 4, "gender_restriction": LeaveType.ANY},
            {"name": "Maternity Leave", "description": "Fully paid leave for female employees.", "days_allocated": 14, "gender_restriction": LeaveType.FEMALE},
            {"name": "Paternity Leave", "description": "Leave for fathers upon the birth of a child.", "days_allocated": 3, "gender_restriction": LeaveType.MALE},
            {"name": "Marriage Leave", "description": "Leave granted for the employee's own marriage.", "days_allocated": 4, "gender_restriction": LeaveType.ANY},
            {"name": "Bereavement Leave", "description": "Leave for the death of close relatives.", "days_allocated": 3, "gender_restriction": LeaveType.ANY},
            {"name": "Circumcision Leave", "description": "Leave granted for the circumcision of the employee's son.", "days_allocated": 1, "gender_restriction": LeaveType.MALE},
            {"name": "Surgery Leave", "description": "Leave for a spouse or dependent child's surgery.", "days_allocated": 2, "gender_restriction": LeaveType.ANY},
            {"name": "Civic Duties Leave", "description": "Leave for civic responsibilities such as voting or jury duty.", "days_allocated": 1, "gender_restriction": LeaveType.ANY},
            {"name": "Unpaid Leave", "description": "Leave for personal reasons, such as exams or sports events.", "days_allocated": 1, "gender_restriction": LeaveType.ANY},
        ]
        for leave_type in leave_types:
            leave_type, created = LeaveType.objects.update_or_create(**leave_type)
            self.stdout.write(self.style.SUCCESS(f'{leave_type.name} is created')) if created else self.stdout.write(self.style.WARNING(f'{leave_type.name} already created'))
