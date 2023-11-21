from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from auth_app.models.profile import Profile
from ...dtos.AdminInfo import AdminInfo


class Command(BaseCommand):
    help = 'Create initial data for your application'

    def add_arguments(self, parser):
        parser.add_argument('username_admin', type=str,
                            help='Indicates the username of admin account')
        parser.add_argument('email_admin', type=str,
                            help='Indicates the email of admin account')
        parser.add_argument('password_admin', type=str,
                            help='Indicates the password of admin account')

    def handle(self, *args, **options):
        # Your script to create initial data goes here
        self.stdout.write(self.style.SUCCESS(
            'Successfully created initial data'))

        # Example: Create a superuser
        if not User.objects.filter(username='admin').exists():
            admin_info = AdminInfo(
                email=options['email_admin'],
                password=options['password_admin'],
                username=options['username_admin']
            )
            if admin_info.username is None or admin_info.username == '' and \
                    admin_info.email is None or admin_info.email == '' and \
                    admin_info.password is None or admin_info.password == '':
                self.stdout.write(self.style.ERROR(
                    'Superuser created unsuccessfully'))
                return

            user = User.objects.create_superuser(
                admin_info.username or '', admin_info.email, admin_info.password)
            user.save()

            profile = Profile.objects.create(user=user, is_admin=True)
            profile.save()
            self.stdout.write(self.style.SUCCESS(
                'Superuser created successfully'))
