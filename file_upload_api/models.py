from django.db import models


class UploadImage(models.Model):
    image = models.ImageField("Uploaded Image", upload_to='documents/%Y/%m/%d')
