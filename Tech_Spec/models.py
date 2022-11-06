from django.db import models


class file_load(models.Model):
    upload_file = models.FileField()

    def __str__(self):
        return self.fname
