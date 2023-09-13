import os
import cv2
import json
import base64
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
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
    return render(request, 'kirinukiapp/upload_complete.html' ,{'file_name': file_name, 'file_duration': file_duration})

# image生成
def generate_image(request):
    gen_apng()
    _, encing = cv2.imencode("kirinuki/kirinukiapp/result/result.png")
    img_str = encing.tostring()
    img_byte = base64.b64encode(img_str).decode('utf-8')
    img_json = json.dumps({'image': img_byte}).encode('utf-8')
    return JsonResponse({"img_data": img_json})
