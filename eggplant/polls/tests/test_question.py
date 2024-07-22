from django.test import TestCase
from django.urls import reverse

from datetime import datetime, timedelta
from polls.models import Question, Choice

# Create your tests here.

class TestQuestion(TestCase):
    """Test the question of the polls app"""
    def setUp(self):
        self.test_question = Question.objects.create(
            question_text = "Test question 1",
            pub_date=datetime.now(),
        )

    def tearDown(self):
        pass

    def test_question_list_view(self):
        """Test question list view"""
        # Fetch the page and get the http response
        page_url = reverse("polls:question_list")
        response = self.client.get(page_url)
        # Validate that the test question in the setUp
        # is in the list view.
        self.assertEqual(first=200, second=response.status_code,
                         msg="Question listing view")
        # Validate that the test question in the view's context
        # is the one in our test. 
        # Total number of question in the database =
        #     total number of questions in the list
        total_question = Question.objects.count()
        self.assertEqual(first=total_question,
                         second=len(response.context["latest_question_list"]),
                         msg="Number of questions")
        # Validate that the test question did show up in the
        # listing view
        self.assertIn(member=self.test_question.question_text,
                      container=str(response.content),
                      msg="Test question appear in context")

    def test_question_detail_view(self):
        # test that question detail view with the test question
        test_id = self.test_question.id
        # fetch the page and get the http response
        page_url = reverse("polls:question_detail", args=(test_id, ))
        response = self.client.get(page_url)
        # Validate the question detail page in the setUp
        self.assertEqual(first=200, second=response.status_code,
                         msg="Question detail")
        # Validate that the id of the test question is in the context
        id_in_context = response.context["question"].id
        self.assertEqual(first=test_id, 
                         second=id_in_context, 
                         msg="Id of test question in question detail")
        # Validate that the text of the test question is in the question
        # detail
        text_in_context = response.context["question"].question_text
        self.assertEqual(first=self.test_question.question_text,
                        second=text_in_context,
                        msg="Question text of test question is the same as the question detail")
