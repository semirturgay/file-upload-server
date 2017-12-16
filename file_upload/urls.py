from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^api/', include('file_upload_rest.urls', namespace='api'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
