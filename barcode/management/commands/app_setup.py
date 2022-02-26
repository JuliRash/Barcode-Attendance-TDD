from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import sys

from barcode.models import Setup


class Command(BaseCommand):
    help = 'Setup Application from scratch'

    def handle(self, *args, **options):

        try:
            call_command('flush', '--no-input')

            organization_name = input(' Organization Name: ')

            if(organization_name is None or organization_name == ''):
                self.stdout.write(self.style.ERROR(
                    '\nYou must provide an organization name!'))
                sys.exit(1)

            organization_description = input(' Organization Description: ')

            if(organization_description is None or organization_description == ''):
                self.stdout.write(self.style.ERROR(
                    '\nYou must provide an organization description!'))
                sys.exit(1)

            organization_location = input(' Organization Location: ')

            if(organization_location is None or organization_location == ''):
                self.stdout.write(self.style.ERROR(
                    '\nYou must provide an organization location!'))
                sys.exit(1)

            call_command('flush', '--no-input')

            call_command('createsuperuser')

            Setup.objects.create(organization_name=organization_name,
                                 organization_description=organization_description, organization_location=organization_location)

            self.stdout.write(self.style.SUCCESS(
                '\nsuccessfully configured application!'))
        except KeyboardInterrupt:
            self.stderr.write('\nOperation cancelled.')
            sys.exit(1)
