from rest_framework import generics, parsers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from ..types.error_response import ErrorResponse

from ..serializers.change_password import ChangePasswordSerializer


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    parser_classes = [parsers.JSONParser]

    def update(self, request, *args, **kwargs):
        if request.user is None or not request.user.is_authenticated:
            return Response(ErrorResponse.get_error_response(401, "You must login to access this action"), status=status.HTTP_401_UNAUTHORIZED)
        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response(ErrorResponse.get_error_response(400, serializer.errors), status=status.HTTP_400_BAD_REQUEST)

            serializer.update(request.user, serializer.validated_data)
            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(ErrorResponse.get_error_response(500, str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
