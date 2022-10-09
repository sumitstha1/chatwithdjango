from urllib.parse import urlparse
from django.urls import path

from . import views
from .views import RoomApiView

urlpatterns = [

    # API Urls
    path('api/v1/rooms/', views.RoomApiView.as_view()),

    path('', views.rooms, name='rooms'),
    path('<slug:slug>', views.room, name='room'),
]
