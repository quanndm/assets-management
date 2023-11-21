from rest_framework import serializers
from ..models.profile import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    user_name = serializers.CharField(source='user.username')
    last_name = serializers.CharField(source='user.last_name')
    first_name = serializers.CharField(source='user.first_name')
    email = serializers.CharField(source='user.email')
    last_login = serializers.DateTimeField(source='user.last_login')

    class Meta:
        model = Profile
        fields = ["user_id", "user_name", "last_name", "first_name", "email",
                  "date_of_birth", "address", "last_login", "gender", "avatar", "is_admin", "last_modified", "phone_number"]
        # field_mapping = {
        #     'user_id': "userId",
        #     'user_name': "userName",
        #     'last_name': "lastName",
        #     'first_name': "firstName",
        #     'email': "email",
        #     'last_login': "lastLogin",
        #     'date_of_birth': "dateOfBirth",
        #     'address': "address",
        #     'gender': "gender",
        #     'avatar': "avatar",
        #     'is_admin': "isAdmin",
        #     'last_modified': "lastModified",
        #     'phone_number': "phoneNumber"
        # }


class CreateUserProfileSerializer(serializers.Serializer):
    user_name = serializers.CharField(source='user.username')
    last_name = serializers.CharField(source='user.last_name')
    first_name = serializers.CharField(source='user.first_name')
    email = serializers.CharField(source='user.email')


class UpdateUserProfileSerializer(serializers.Serializer):
    user_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    email = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    date_of_birth = serializers.DateField()
    gender = serializers.CharField(required=False, allow_blank=True)
