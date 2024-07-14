import csv
import datetime
from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = "Export data from any Model"

    def add_arguments(self, parser):
        parser.add_argument("model_name", type=str, help="Model name to export data from.")


    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name']
        model = None

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        file_name = f"exported-data-{model_name}-{timestamp}.csv"
    
        for app_config in apps.get_app_configs():
            try:
                model = app_config.get_model(model_name)
                break # Model found
            except LookupError:
                continue
        
        if not model:
            self.stdout.write(self.style.WARNING(f"The model name, {model_name}, does not exist"))
        else:
            data = model.objects.all()
            with open(file_name, "w", newline="") as file:
                csv_writer = csv.writer(file)

                csv_writer.writerow([field.name for field in model._meta.fields]) 
                for obj in data:
                    csv_writer.writerow([getattr(obj, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS("Data exported successfully!"))