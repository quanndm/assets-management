from datetime import datetime
import json
from django.http import HttpRequest
from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.decorators import api_view, permission_classes
from core.utils.send_mail import send_email
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from ..types.gender_enum import Gender
from ..validators.email import isValidEmail
from ..validators.update_user_profile import update_user_profile
from ..validators.create_user_profile import create_user_profile
from ..models.profile import Profile
from ..serializers.user_profile import UpdateUserProfileSerializer, UserProfileSerializer, CreateUserProfileSerializer
from ..types.error_response import ErrorResponse
from ..helpers.generate_password import generate_password


class UserProfileViewSet(viewsets.ModelViewSet, generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    # method: GET
    def list(self, request: HttpRequest):
        profile = self.queryset.get(user=request.user)

        if profile is None:
            return Response(ErrorResponse.get_error_response(404, "User not found"), status=status.HTTP_404_NOT_FOUND)

        if profile.is_admin is False:
            return Response(ErrorResponse.get_error_response(403, "You don't have permission to access this action"), status=status.HTTP_403_FORBIDDEN)

        return Response(
            self.serializer_class(self.queryset.all(), many=True).data,
            status=status.HTTP_200_OK
        )

    # method: GET, pk: user_id
    def retrieve(self, request: HttpRequest, pk: int | None = None):
        if not request.user.is_authenticated:
            return Response(ErrorResponse.get_error_response(401, "You must login to access this action"), status=status.HTTP_401_UNAUTHORIZED)

        if pk is None:
            return Response(ErrorResponse.get_error_response(400, "User id is required"), status=status.HTTP_400_BAD_REQUEST)

        try:
            profile = self.queryset.get(user=pk)
            profile_current_user = self.queryset.get(user=request.user)

            if profile_current_user is None or profile is None:
                return Response(ErrorResponse.get_error_response(404, "User not found"), status=status.HTTP_404_NOT_FOUND)

            if profile_current_user.is_admin:
                return Response(self.serializer_class(profile).data, status=status.HTTP_200_OK)

            if not profile.is_admin or profile.user.pk != request.user.pk:
                return Response(ErrorResponse.get_error_response(403, "You don't have permission to access this action"), status=status.HTTP_403_FORBIDDEN)

            return Response(self.serializer_class(profile).data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(ErrorResponse.get_error_response(500, "Internal server error"), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # method : PUT
    def update(self, request, pk=None):
        if pk is None:
            return Response(ErrorResponse.get_error_response(400, "User id is required"), status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer = UpdateUserProfileSerializer(data=request.data)

            if not serializer.is_valid():
                return Response(ErrorResponse.get_error_response(400, "error"), status=status.HTTP_400_BAD_REQUEST)

            obj = {
                "user_name": serializer.data["user_name"],
                "last_name": serializer.data["last_name"],
                "first_name": serializer.data["first_name"],
                "email": serializer.data["email"],
                "date_of_birth": serializer.data["date_of_birth"],
                "address": serializer.data["address"],
                "gender": serializer.data["gender"],
            }

            validate = update_user_profile(obj, pk)

            if not validate[0]:
                return Response({"message": validate[1]}, status=status.HTTP_400_BAD_REQUEST)
            # cach 1

            # User.objects.filter(pk=pk).update(username=obj["user_name"],last_name=obj["last_name"],first_name=obj["first_name"],email=obj["email"])

            # Profile.objects.filter(user=pk).update(DOB=(datetime.strptime(obj["DOB"], '%d-%m-%Y').date() if obj["DOB"] else ""),address=obj["address"],description=obj["description"],gender=obj["gender"])

            # cach 2
            with transaction.atomic():
                user = User.objects.get(pk=pk)
                user.username = obj["user_name"] or ''
                user.last_name = obj["last_name"] or ''
                user.first_name = obj["first_name"] or ''
                # user.email = obj["email"] or ''
                user.save(update_fields=['username',
                                         'first_name', 'last_name'])

                profile = Profile.objects.get(user=pk)
                profile.date_of_birth = datetime.strptime(
                    obj["date_of_birth"] or '', "%Y-%m-%d")
                profile.address = obj["address"] or ''
                profile.gender = obj["gender"] or ''
                profile.save(update_fields=[
                    'date_of_birth', 'gender', 'address'])

                return Response({"message": "Update success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Update fail!"}, status=status.HTTP_400_BAD_REQUEST)

    # method: PATCH
    def partial_update(self, request, pk=None):
        return Response({"message": "API does not support method: PATCH"}, status=status.HTTP_400_BAD_REQUEST)

    # method: POST
    def create(self, request,  *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(ErrorResponse.get_error_response(401, "You must login to access this action"), status=status.HTTP_401_UNAUTHORIZED)

        profile = self.queryset.get(user=request.user)
        if profile is None:
            return Response(ErrorResponse.get_error_response(404, "User not found"), status=status.HTTP_404_NOT_FOUND)

        if not profile.is_admin:
            return Response(ErrorResponse.get_error_response(403, "You don't have permission to access this action"), status=status.HTTP_403_FORBIDDEN)

        try:
            serializer = CreateUserProfileSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

            obj = {
                "user_name": serializer.data["user_name"],
                "last_name": serializer.data["last_name"],
                "first_name": serializer.data["first_name"],
                "email": serializer.data["email"],
            }
            validate = create_user_profile(obj)

            if not validate[0]:
                return Response({"message": validate[1]}, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():
                password = generate_password()
                user = User.objects.create(
                    username=obj["user_name"],
                    last_name=obj["last_name"],
                    first_name=obj["first_name"],
                    email=obj["email"],
                    password=generate_password()
                )
                user.save()

                profile = Profile.objects.create(
                    user=user, gender=Gender.MALE.value)
                profile.save()
                send_email(
                    subject=f"Account Created!",
                    message="This email include password, username, and email to login the website",
                    html_message=f"""
                        <div>
                            <h1>Your account info<h1>
                            <p>Username: {user.username}</p>
                            <p>Password: {password}</p>
                            <p>Email: {user.email}</p>
                            <p>You can you info above to login the website</p>
                        <div>
                    """,
                    to_email=[user.email],
                )
                return Response({"message": "Create user success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(ErrorResponse.get_error_response(500, "Internal server error"), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def forgot_pwd(request: HttpRequest):
    email: str | None = None
    try:
        email = json.loads(request.body).get("email")
    except:
        email = None

    if email is None:
        return Response(ErrorResponse.get_error_response(400, "Email can not be null"), status=status.HTTP_400_BAD_REQUEST)
    if not isValidEmail(email):
        return Response(ErrorResponse.get_error_response(400, "Email is invalid"), status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).count() == 0:
        return Response(ErrorResponse.get_error_response(404, "Email is not registered"), status=status.HTTP_404_NOT_FOUND)

    # send mail to user to reset password
    send_email(
        subject=f"Reset password for {email}",
        message="This is a test mail in message",
        html_message="<h1>This is a test mail in HTML message</h1>",
        to_email=[email],
    )

    return Response({"message": "If you have registered, you can receive an email to reset password"}, status=status.HTTP_200_OK)
