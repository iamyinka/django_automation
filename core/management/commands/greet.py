from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = "A command to welcome the user"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Specify a user to welcome")

    # Declare the handle method
    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f"Hello {name}, How are you today? "
        self.stdout.write(greeting)