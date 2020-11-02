from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from user import views
app_name = 'user'
urlpatterns = [
    path('login/',views.UserViewSet.as_view({'post': 'login'})),
    path('register/',views.UserViewSet.as_view({'post': 'register'})),
    re_path('^media/?P<path>.*$',serve,{'document_root': settings.MEDIA_URL}),
]