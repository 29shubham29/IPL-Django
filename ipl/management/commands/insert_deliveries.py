import csv
import os
from django.core.management.base import BaseCommand, CommandError
from ipl.models import Deliveries

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file_path = '/home/shubham/ipl_django/ipl/management/commands/deliveries.csv'
        insert_count = Deliveries.objects.from_csv(file_path)
        print ("{} records inserted".format(insert_count))