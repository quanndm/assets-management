from django.core.mail import send_mail
from django.conf import settings


def send_email(subject: str,
               message: str,
               html_message: str | None,
               from_email: str | None,
               to_email: list[str],
               ):
    sender_email = settings.EMAIL_HOST_USER
    if from_email is None:
        from_email = sender_email

    send_mail(
        subject=subject,
        message=message,
        html_message=html_message,
        from_email=from_email,
        recipient_list=to_email,
        fail_silently=False,
    )
