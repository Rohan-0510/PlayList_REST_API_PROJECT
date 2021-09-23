
from django.contrib import admin
from django.urls import path
from api.views import playlist_option,playlist_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playlist_option/',playlist_option),
    path('playlist_option/<str:name>',playlist_option),
    path('playlist_list/',playlist_list.as_view()),
]
