from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from app import views

app_name = 'app'
urlpatterns = [
    path('teacher/',views.TeacherAPIView.as_view()),
    path('teacher/<str:id>/',views.TeacherAPIView.as_view()),
    re_path(r'^media/(?P<path>.*)',serve,{'document_root': settings.MEDIA_ROOT})
]