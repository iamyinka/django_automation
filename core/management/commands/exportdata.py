import csv
import datetime
from django.core.management.base import BaseCommand

from core.models import Student

class Command(BaseCommand):
    help = "Export data from DB"

    def handle(self, *args, **kwargs):

        # Retrieve all Data from DB
        students = Student.objects.all()

        # Create output file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        output_file = f"exported-data-{timestamp}.csv"
        
        # Open and write to file
        with open(output_file, "w", newline="") as file:
            writer = csv.writer(file)

            # Write CVS Column headers
            writer.writerow(["Roll #", "Student Name", "Age"])

            for student in students:
                writer.writerow([student.roll_no, student.name, student.age])

        # Print success message
        self.stdout.write(self.style.SUCCESS("Data exported successfully!"))