from django.http import HttpRequest
from rest_framework import viewsets, status
from ..serializers.CategorySerializer import CategorySerializer
from ..models.Category import Category
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser)

    def list(self, request: HttpRequest, *args, **kwargs):
        categories = Category.objects.all()
        return Response(
            self.serializer_class(categories, many=True).data,
            status=status.HTTP_200_OK,
        )
