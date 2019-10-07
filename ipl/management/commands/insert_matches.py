import csv
import os
from django.core.management.base import BaseCommand, CommandError
from ipl.models import Matches
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file_path = '/home/shubham/ipl_django/ipl/management/commands/matches.csv'
        insert_count = Matches.objects.from_csv(file_path)
        print ("{} records inserted".format(insert_count))