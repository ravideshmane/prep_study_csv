import mimetypes

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import StudentForm
from .models import StudentRecord


def uploadCSV(request):
    # function to upload csv file
    if request.method == 'GET':
        csv = StudentRecord.objects.all()
        file_list = list()
        for file in csv:
            file_list.append(file.csv_file)
        form = StudentForm()
        return render(request, 'csv.html', {'form': form, 'csv_files':file_list})
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The file has been uploaded successfully!')
        return render(request, 'csv.html', {'form': form})


def download(request):
    # fill these variables with real values

    fl_path = 'C:/Users/lenovo/Desktop/Demo.csv'
    filename = 'Demo.csv'
    fl = open(fl_path, 'r')
    mime_type= mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
