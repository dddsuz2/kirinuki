from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import FileUpload
from .forms import FileUploadForm
import os
from django.views.generic.edit import FormView
# Create your views here.

UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/media/'  # アップロードしたファイルを保存するディレクトリ
FILE_NAME = ''

# アップロードされたファイルのハンドル
def handle_uploaded_file(f):
    path = os.path.join(UPLOAD_DIR, f.name)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# ファイルアップロード
def upload(request):
    global FILE_NAME
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_file = request.FILES['attach']
            handle_uploaded_file(upload_file)
            FILE_NAME = upload_file.name
            return redirect('upload_complete')  # アップロード完了画面にリダイレクト
    else:
        form = FileUploadForm()
    return render(request, 'kirinukiapp/upload.html', {'form': form})


# ファイルアップロード完了
def upload_complete(request):
    return render(request, 'kirinukiapp/upload_complete.html' ,{'file': FILE_NAME})