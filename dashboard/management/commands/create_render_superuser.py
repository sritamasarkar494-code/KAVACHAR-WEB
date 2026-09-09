import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create or update the Render superuser."

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.getenv("SUPERADMIN_USERNAME")
        email = os.getenv("SUPERADMIN_EMAIL")
        password = os.getenv("SUPERADMIN_PASSWORD")

        if not username or not email or not password:
            self.stdout.write(
                self.style.ERROR(
                    "SUPERADMIN_USERNAME, SUPERADMIN_EMAIL, "
                    "and SUPERADMIN_PASSWORD must be set."
                )
            )
            return

        user, created = User.objects.get_or_create(
            username=username
        )

        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Superuser '{username}' created successfully."
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Superuser '{username}' already existed and was updated."
                )
            )