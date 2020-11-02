from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from api import views

app_name = 'api'
urlpatterns = [
    path('books/', views.BookAPIView.as_view()),
    path('books/<str:id>/', views.BookAPIView.as_view()),
    re_path(r'^media/?P<path>.*', serve, {'document_root': settings.MEDIA_URL}),

    path('gen/', views.BookGenericAPIView.as_view()),
    path('gen/<str:id>/', views.BookGenericAPIView.as_view()),

    path('login/', views.BookViewSet.as_view({'post': 'login'})),
    path('login/<str:id>/', views.BookViewSet.as_view({'post': 'login'})),
]
