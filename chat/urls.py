from django.urls import path, include
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("addfriend/<str:name>", views.addFriend, name="addFriend"),
    path("chat/<str:username>", views.chat, name="chat"),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
