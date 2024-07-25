from django.test import TestCase
from django.urls import reverse

from datetime import datetime, timedelta
from polls.models import Question, Choice

# Create your tests here.

class TestQuestionRecent(TestCase):
    """Test the question of the polls app"""
    def test_page_ok(self):
        """Test getting the page"""
        page_url = reverse("polls:question_list_recent")
        response = self.client.get(page_url)
        self.assertEqual(first=200, second=response.status_code,
                         msg="question_list_recent ok")
    
    def test_recent_2(self):
        """The recent question only return 2 questions.
            When display all questions, the length of
            the list will be equal to the len of the objects.
        """
        # Create some test questions
        for i in range(1, 6):
            Question.objects.create(
                question_text=f"question {i}",
                pub_date=datetime(year=2024, month=8, day=i)
            )
        question_list = Question.objects.all()
        
        # Checkbox status = None
        page_url = reverse("polls:question_list_recent")
        post_data = {"recent": ""}
        response = self.client.post(path=page_url, data=post_data)
        self.assertEqual(first=200, second=response.status_code, 
                         msg="post to question_list_recent: None")
        total = Question.objects.count()
        
        self.assertEqual(first=total, 
                         second=len(response.context["latest_question_list"]),
                         msg="All questions in the context")
        # Checkbox status = on
        post_data = {"recent": "on"}
        response = self.client.post(path=page_url, data=post_data)
        self.assertEqual(first=200, second=response.status_code, 
                         msg="post to question_list_recent: on")
        self.assertEqual(first=2, 
                         second=len(response.context["latest_question_list"]),
                         msg="Only two questions in the context")