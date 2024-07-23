from django.test import TestCase
from django.urls import reverse

from datetime import datetime, timedelta
from polls.models import Question, Choice

# Create your tests here.

class TestQuestionVote(TestCase):
    """Test the question of the polls app"""
    def setUp(self):
        self.test_question = Question.objects.create(
            question_text = "Test question 1",
            pub_date=datetime.now(),
        )

    def tearDown(self):
        pass

    def test_question_vote_view(self):
        pass