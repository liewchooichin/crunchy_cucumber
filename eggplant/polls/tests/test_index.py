from django.test import TestCase
# to test reverse urls
from django.urls import reverse

# Create your tests here
from django.conf import settings
from django.conf.urls.static import static
from eggplant import urls as main_urls

class TestPolls(TestCase):
    """Test for polls app"""
    def test_index(self):
        """Test polls/index/"""
        response = self.client.get(path="/polls/")
        self.assertEqual(first=200, second=response.status_code,
                         msg="polls/index/")

    def test_reverse_index(self):
        """Test reverse index"""
        reverse_url = reverse("polls:index")
        self.assertEqual(reverse_url, "/polls/")

