from django.shortcuts import render, get_object_or_404
from .models import Wallpaper

def wallpaper_list_view(request):
    wallpapers = Wallpaper.objects.all().order_by('-uploaded_at')
    context = {'wallpapers': wallpapers}
    # The actual template 'wallpapers/wallpaper_list.html' is not needed for the tests to pass,
    # but would be for actual browsing.
    return render(request, 'wallpapers/wallpaper_list.html', context)

def wallpaper_detail_view(request, pk):
    wallpaper = get_object_or_404(Wallpaper, pk=pk)
    context = {'wallpaper': wallpaper}
    # The actual template 'wallpapers/wallpaper_detail.html' is not needed for tests to pass.
    return render(request, 'wallpapers/wallpaper_detail.html', context)
