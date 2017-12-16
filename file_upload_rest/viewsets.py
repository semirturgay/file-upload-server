from rest_framework import viewsets

from file_upload_api.models import UploadImage
from file_upload_rest.serializers import UploadImageSerializer


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer
