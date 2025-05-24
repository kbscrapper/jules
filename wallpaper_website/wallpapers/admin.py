from django.contrib import admin
from .models import Wallpaper, Tag

# Custom Admin for Wallpaper
class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail', 'uploaded_at') # Added image_thumbnail
    list_filter = ('tags', 'uploaded_at') # Added uploaded_at
    search_fields = ('title', 'description')
    readonly_fields = ('image_thumbnail_display',) # For displaying image in detail view

    def image_thumbnail(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "No Image"
    image_thumbnail.short_description = 'Thumbnail'

    def image_thumbnail_display(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" style="max-width: 300px; max-height: 300px;" />', obj.image.url)
        return "No Image"
    image_thumbnail_display.short_description = 'Image Preview'


# Custom Admin for Tag (Optional, but good for consistency)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Wallpaper, WallpaperAdmin)
admin.site.register(Tag, TagAdmin) # Register Tag with its custom admin
