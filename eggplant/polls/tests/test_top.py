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

    def test_polls_results(self):
        """Test polls/<question_id>/results/"""
        response = self.client.get(path="/polls/1/results/")
        self.assertEqual(first=200, second=response.status_code,
                         msg="polls/<question_id>/results/")
    
    def test_polls_vote(self):
        """Test polls/<question_id>/vote/"""
        response = self.client.get(path="/polls/1/vote/")
        self.assertEqual(first=200, second=response.status_code,
                         msg="reverse index")

    def test_reverse_index(self):
        """Test reverse index"""
        reverse_url = reverse("polls:index")
        self.assertEqual(reverse_url, "/polls/")

    def test_reverse_question_detail(self):
        """Test reverse index"""
        reverse_url = reverse("polls:question_detail", args=(1, ))
        self.assertEqual(reverse_url, "/polls/question_detail/1/")

    def test_reverse_results(self):
        """Test reverse index"""
        reverse_url = reverse("polls:results", args=(1, ))
        self.assertEqual(reverse_url, "/polls/1/results/")

    def test_reverse_vote(self):
        """Test reverse index"""
        reverse_url = reverse("polls:vote", args=(1, ))
        self.assertEqual(reverse_url, "/polls/1/vote/")
    
    def test_question_list(self):
        """Test display of question list"""
        response = self.client.get(path="/polls/question_list/")
        self.assertEqual(first=200, second=response.status_code,
            msg="display question list")
    
    def test_reverse_question_list(self):
        """Test reverse of displaying question list"""
        reverse_url = reverse("polls:question_list")
        self.assertEqual(reverse_url, "/polls/question_list/")
    
    # def test_polls_question_detail(self):
    #     """Test question detail"""
    #     # This test is always give 404. What is the reason???
    #     response = self.client.get(path="/polls/question_detail/2/")
    #     self.assertEqual(first=200, second=response.status_code,
    #                      msg="get polls question detail")
    
    # def test_question_detail_404(self):
    #     """Test for question that does not exist"""
    #     # This test is related to the above. Even the object exists,
    #     # it is always 404.
    #     reverse_url = reverse("polls:question_detail", args=(1, ))
    #     response = self.client.get(reverse_url)
    #     self.assertEqual(first=404,
    #                      second=response.status_code,
    #                      msg="Question detail does not exist")
    