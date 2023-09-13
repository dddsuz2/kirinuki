from django.urls import path

from . import views

urlpatterns = [
    #path("", views.Upload.upload_file, name="index"),
    path('upload/', views.upload, name='upload'),
    path('upload_complete/', views.upload_complete, name='upload_complete'),
    path('generate_gif/', views.generate_image, name='generate_image'),
]