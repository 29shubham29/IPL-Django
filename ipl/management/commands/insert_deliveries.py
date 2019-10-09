import csv
import os
from django.core.management.base import BaseCommand, CommandError
from ipl.models import Delivery
from django.db import transaction

class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **kwargs):
        file_path = '/home/shubham/ipl_django/ipl/management/commands/deliveries.csv'
        insert_count = Delivery.objects.from_csv(file_path,drop_constraints=False, drop_indexes=False)
        print ("{} records inserted".format(insert_count))