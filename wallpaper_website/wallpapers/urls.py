from django.urls import path
from . import views  # Assuming views.py will be created or already exists

app_name = 'wallpapers'

urlpatterns = [
    # These views need to be defined in wallpapers/views.py
    path('', views.wallpaper_list_view, name='wallpaper_list'),
    path('wallpaper/<int:pk>/', views.wallpaper_detail_view, name='wallpaper_detail'),
]
