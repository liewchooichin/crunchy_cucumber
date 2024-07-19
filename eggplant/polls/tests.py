from django.test import TestCase
# to test reverse urls
from django.urls import reverse

# Create your tests here.

class TestPolls(TestCase):
    """Test for polls app"""

    def test_index(self):
        """Test polls/index/"""
        response = self.client.get(path="/polls/")
        self.assertEqual(first=200, second=response.status_code,
                         msg="polls/index/")
    
    def test_polls_detail(self):
        """Test polls/<question_id>/"""
        response = self.client.get(path="/polls/30/")
        self.assertEqual(first=200, second=response.status_code,
                         msg="polls/<question_id>")

    def test_polls_results(self):
        """Test polls/<question_id>/polls-results/"""
        response = self.client.get(path="/polls/30/results/")
        self.assertEqual(first=200, second=response.status_code,
                         msg="polls/<question_id>/results/")
    
    def test_polls_vote(self):
        """Test polls/<question_id>/polls-vote/"""
        response = self.client.get(path="/polls/30/vote/")
        self.assertEqual(first=200, second=response.status_code,
                         msg="reverse polls-index")

    def test_reverse_index(self):
        """Test reverse index"""
        reverse_url = reverse("polls:polls-index")
        self.assertEqual(reverse_url, "/polls/")

    def test_reverse_detail(self):
        """Test reverse index"""
        reverse_url = reverse("polls:polls-detail", args=(30, ))
        self.assertEqual(reverse_url, "/polls/30/")

    def test_reverse_results(self):
        """Test reverse index"""
        reverse_url = reverse("polls:polls-results", args=(30, ))
        self.assertEqual(reverse_url, "/polls/30/results/")

    def test_reverse_vote(self):
        """Test reverse index"""
        reverse_url = reverse("polls:polls-vote", args=(30, ))
        self.assertEqual(reverse_url, "/polls/30/vote/")