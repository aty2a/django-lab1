

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView


class HomeTests(TestCase):

    def test_home_view_status_code(self):
        url = reverse('home')  # Use standard quotes
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Ensure status code is 200

    def test_home_url_resolves_home_view(self):
        view = resolve('/')  # Use standard quotes and correct URL
        self.assertEqual(view.func.view_class, HomePageView)  # Ensure correct view is resolved



