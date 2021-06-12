from django import forms

from .models import StudentRecord


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.csv']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

    # coupling_file = forms.FileField(label='XML File Upload:',
    #                                 required=True, validators=[validate_file_extension])
    #


class StudentForm(forms.ModelForm):
     csv_file = forms.FileField(label='CSV File Upload:', required=True, validators=[validate_file_extension])
     class Meta:
         model = StudentRecord
         fields = '__all__'



