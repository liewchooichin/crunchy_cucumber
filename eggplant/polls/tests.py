from django.test import TestCase

# Create your tests here.

class TestPolls(TestCase):
    """Test for polls app"""

    def test_index(self):
        """Test polls/index/"""
        response = self.client.get(path="/polls/")
        self.assertEqual(first=200, second=response.status_code,
                         msg="polls/index 200")