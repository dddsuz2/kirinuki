import os
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import FileUpload
from .forms import FileUploadForm
from django.views.generic.edit import FormView
from .gen_gif import convert_movie_to_jpgs
# Create your views here.


# ファイルアップロード
def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_complete')  # アップロード完了画面にリダイレクト
    else:
        form = FileUploadForm()
    return render(request, 'kirinukiapp/upload.html', {'form': form})


# ファイルアップロード完了
def upload_complete(request):
    uploaded_file = FileUpload.objects.first()
    file_name = os.path.basename(uploaded_file.filename)
    file_duration = int(uploaded_file.duration)
    convert_movie_to_jpgs(uploaded_file.filename)
    return render(request, 'kirinukiapp/upload_complete.html' ,{'file_name': file_name, 'file_duration': file_duration})
