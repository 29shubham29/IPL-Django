import csv
import os
from django.core.management.base import BaseCommand, CommandError
from ipl.models import Match
from django.db import transaction

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = '/home/shubham/ipl_django/ipl/management/commands/matches.csv'

class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.drop_constraints=False
        self.drop_indexes=False
        insert_count = Match.objects.from_csv(file_path,drop_constraints=False, drop_indexes=False)
        print ("{} records inserted".format(insert_count))