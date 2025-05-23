from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Wallpaper, Tag
import os # For cleaning up files if necessary

class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name='Nature')

    def test_tag_creation(self):
        tag = Tag.objects.get(name='Nature')
        self.assertEqual(tag.name, 'Nature')
        self.assertEqual(str(self.tag), 'Nature')

class WallpaperModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name='Abstract')
        # For model tests, ImageField doesn't strictly need a file if not testing file operations
        # However, to be consistent with view tests and ensure model can save with it:
        self.dummy_image_model = SimpleUploadedFile(
            name="model_test_image.jpg", 
            content=b"dummy_content_for_model", 
            content_type="image/jpeg"
        )
        self.wallpaper = Wallpaper.objects.create(
            title='Cool Abstract Design', 
            description='A test wallpaper',
            image=self.dummy_image_model 
        )
        self.wallpaper.tags.add(self.tag)

    def test_wallpaper_creation(self):
        wallpaper = Wallpaper.objects.get(title='Cool Abstract Design')
        self.assertEqual(wallpaper.title, 'Cool Abstract Design')
        self.assertTrue(wallpaper.image.name.startswith('wallpapers/model_test_image'))
        self.assertEqual(str(self.wallpaper), 'Cool Abstract Design')

    def test_wallpaper_tags(self):
        self.assertEqual(self.wallpaper.tags.count(), 1)
        self.assertEqual(self.wallpaper.tags.first().name, 'Abstract')
    
    def tearDown(self):
        # Clean up the dummy image file if it exists and has a path
        if self.wallpaper.image and hasattr(self.wallpaper.image, 'path'):
            if os.path.exists(self.wallpaper.image.path):
                try:
                    os.remove(self.wallpaper.image.path)
                except OSError:
                    # Handle cases where the file might be locked or already removed
                    pass


class WallpaperViewTest(TestCase):
    def setUp(self):
        self.dummy_image_view = SimpleUploadedFile(
            name='view_test_image.jpg',
            content=b'dummy_content_for_view',
            content_type='image/jpeg'
        )
        self.wallpaper = Wallpaper.objects.create(
            title='Test View Wallpaper', 
            image=self.dummy_image_view
        )
        # We need URLs for the views, so wallpaper_list and wallpaper_detail must exist
        # This requires setting up wallpaper_website/wallpapers/urls.py and including it in project urls.py
        # Assuming these are set up as per previous subtasks.

    def test_wallpaper_list_view(self):
        # Ensure the app's URLs are loaded for reverse() to work
        # This typically means wallpaper_website.urls includes wallpapers.urls
        # and wallpapers.urls has app_name = 'wallpapers'
        try:
            url = reverse('wallpapers:wallpaper_list')
        except Exception as e:
            self.fail(f"Could not reverse 'wallpapers:wallpaper_list'. Is urls.py configured correctly? Error: {e}")
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.wallpaper.title)
        self.assertContains(response, self.wallpaper.image.url) # Check image URL is present

    def test_wallpaper_detail_view(self):
        try:
            url = reverse('wallpapers:wallpaper_detail', args=[self.wallpaper.pk])
        except Exception as e:
            self.fail(f"Could not reverse 'wallpapers:wallpaper_detail'. Is urls.py configured correctly? Error: {e}")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.wallpaper.title)
        self.assertContains(response, self.wallpaper.image.url) # Check image URL is present

    def tearDown(self):
        # Clean up the dummy image file if it exists and has a path
        if self.wallpaper.image and hasattr(self.wallpaper.image, 'path'):
            if os.path.exists(self.wallpaper.image.path):
                try:
                    os.remove(self.wallpaper.image.path)
                except OSError:
                    pass
