from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('getvalue/', views.getValue),
    path('chat/', views.chat, name='chat'),
    # urls.py
path("chat/<int:id>/", views.chat_detail, name="chat_detail"),
]