import os.path

from django.db import models

import uuid
# Create your models here.


def get_upload_path(instance, filename):
    return os.path.join(str(instance.folder.uid), filename)

class Folder(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    created_at = models.DateField(auto_now=True)


class Files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to='')
    created_at = models.DateField(auto_now=True)
