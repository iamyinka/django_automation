import csv
from typing import Any
from django.core.management.base import BaseCommand, CommandParser, CommandError

# "C:\Users\iAmYinka\Desktop\customer_demo_records.csv"

# from core.models import Student
from django.apps import apps

class Command(BaseCommand):

    help = "Data import tool"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("model", type=str, help="Enter a model name")
        parser.add_argument("file_path", type=str, help="Provide a file path")

    def handle(self, *args: Any, **options: Any) -> str | None:
        help = "Automate data import to DB"

        xlsfile = options['file_path']
        model_name = options["model"]

        self.stdout.write(self.style.SUCCESS(xlsfile))
        self.stdout.write(self.style.SUCCESS(model_name.title()))

        # For 1 Data

        # Student.objects.get_or_create(
        #     roll_no= 1001, name = "Test User 1", age = 25
        # )

        # Populate data from a list

        # dataset = [
        #     { "roll_no": 1001, "name": "Test User 2", "age": 35 },
        #     { "roll_no": 1002, "name": "Test User 3", "age": 18 },
        #     { "roll_no": 1003, "name": "Test User 4", "age": 27 },
        #     { "roll_no": 1004, "name": "Test User 5", "age": 19 },
        # ]

        # for data in dataset:
        #     duplicate_row = data["roll_no"]
        #     if not Student.objects.filter(roll_no=data["roll_no"]).exists():
        #        Student.objects.create(
        #             roll_no= data["roll_no"], name = data["name"], age = data["age"]
        #         )
        #     else:
        #        self.stdout.write(self.style.WARNING(f"Student with roll #: {duplicate_row} exists already"))
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = app_config.get_model(model_name=model_name)
                break # Model is found
            except LookupError:
                continue

        if not model:
            raise CommandError(f"Model {model_name} does not exist")


        # Populate DB from CSV file
        with open(xlsfile, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
                # roll_no = row["roll_no"]
                # duplicate_row = Student.objects.filter(roll_no=roll_no).exists()
                # if not duplicate_row:
                #     Student.objects.create(
                #             **row  )
                # else:
                #     self.stdout.write(self.style.WARNING(f"Student with roll #: {roll_no} exists already"))

        self.stdout.write(self.style.SUCCESS("Data imported successfully!"))