import os
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import FileUpload
from .forms import FileUploadForm
from django.views.generic.edit import FormView
from .gen_gif import convert_movie_to_jpgs, duration, gen_apng

# Create your views here.

file = None

def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            global file
            file = request.FILES['attach']
            return redirect('upload_complete')  # アップロード完了画面にリダイレクト
    else:
        form = FileUploadForm()
    return render(request, 'kirinukiapp/upload.html', {'form': form})


# ファイルアップロード完了
def upload_complete(request):
    uploaded_file = file
    file_name = uploaded_file.name
    file_path = f"kirinuki/media/media/{file_name}"
    file_duration = duration(file_path)
    convert_movie_to_jpgs(file_path)
    gen_apng()
    return render(request, 'kirinukiapp/upload_complete.html' ,{'file_name': file_name, 'file_duration': file_duration})
