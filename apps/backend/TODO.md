- example of view send email, can be used when create auth for this app

```python
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from core.utils.send_mail import send_email
from rest_framework.permissions import AllowAny
# Create your views here.


@api_view(['GET'])
@permission_classes((AllowAny, ))
def do_send_mail(request: HttpRequest) -> HttpResponse:
    """
    Send mail to the user
    """
    send_email(
        subject="Test mail",
        message="This is a test mail in message",
        html_message="<h1>This is a test mail in HTML message</h1>",
        to_email=["to@example.com"]
    )
    return HttpResponse("Mail sent successfully")

```
