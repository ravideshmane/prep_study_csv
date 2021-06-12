from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class StudentRecord(models.Model):
    csv_file = models.FileField(upload_to="student_media/")

    def __str__(self):
        return str(self.csv_file)
