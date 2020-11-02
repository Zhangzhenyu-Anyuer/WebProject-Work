from django.urls import path

from user import views

app_name = 'user'
urlpatterns = [
    path('index/', views.index, name='index'),

    path('user_view/',views.UserView.as_view()),
    path('user_view/<str:id>/',views.UserView.as_view()),
    path('userView/',views.User_View.as_view()),
    path('userView/<str:id>/',views.User_View.as_view()),
]
