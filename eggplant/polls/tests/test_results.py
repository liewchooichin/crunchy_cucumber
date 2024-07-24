from django.test import TestCase
from django.urls import reverse

from datetime import datetime, timedelta
from polls.models import Question, Choice

# Create your tests here.

class TestVoteResult(TestCase):
    """Test the question of the polls app"""
    def setUp(self):
        # The question
        self.test_question = Question.objects.create(
            question_text = "Question 1",
            pub_date=datetime.now(),
        )
        # The choice
        # Can be added in two ways:
        # method 1
        self.test_choice = Choice.objects.create(
            choice_text="Choice 1",
            votes=1,
            question=self.test_question, # point to the question
        )
        # method 2
        self.test_question.choice_set.create(
            choice_text="Choice 2", votes=2
        )
    def tearDown(self):
        pass
    def test_vote_result_view(self):
        """Validate that the view is ok"""
        page_url = reverse("polls:vote_results", args=(self.test_question.id, ))
        response = self.client.get(page_url)
        self.assertEqual(first=200, second=response.status_code)
        """Test for template name"""
        self.assertTemplateUsed(
            response=response, 
            template_name="polls/vote_results.html"
            )
        """Check for the choice_text and votes in the context"""
        test_context = {
            "question": self.test_question,
        }
        self.assertContains(response=response, 
                            text=self.test_question.question_text,)
        for item in self.test_question.choice_set.all():
            self.assertContains(response=response,
                            text=item.choice_text)
            self.assertContains(response=response,
                            text=item.votes)


