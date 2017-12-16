from django.conf.urls import url, include
from rest_framework import routers

from file_upload_rest.viewsets import ImageUploadViewSet

router = routers.DefaultRouter()
router.register('images', ImageUploadViewSet, 'images')
urlpatterns = [
    url(r'^', include(router.urls))
]
