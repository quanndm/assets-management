from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password')

    def validate_old_password(self, value: str):
        user = self.context['request'].user

        if not user.check_password(value):
            raise serializers.ValidationError(
                {"message": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        user = User.objects.get(id=instance.id)
        user.set_password(validated_data['password'])
        user.save()

        return instance
