from django.test import TestCase
from django.urls import reverse

from datetime import datetime

from polls.models import Question, Choice

# Create your tests here.

class TestChoice(TestCase):
    """Test cases for Choice"""
    def setUp(self):
        """Set up the test data"""
        self.test_question = Question.objects.create(
            question_text = "Question",
            pub_date = datetime.today(),
        )
        # more than 30 chars, the __str__ is supposed to limit
        # the return string to only 30 chars
        self.test_choice_1 = Choice.objects.create(
            id=3003, # an unlikely id
            choice_text = "1234567890 1234567890 1234567890 1234567890",
            question = self.test_question
        )
        self.test_choice_2 = Choice.objects.create(
            id=3004, # an unlikely id
            choice_text = "1234567890 1234567890 1234567890 1234567890",
            question = self.test_question
        )
    def test_choice_data(self):
        """Test that the test data is what was created
            in the database.
        """
        question = Question.objects.create(
            question_text = "question 1",
            pub_date=datetime(year=2024, month=8, day=1),
        )
        choice = Choice.objects.create(
            choice_text = "choice 1",
            votes = 0,
            question = question
        )
        
        choice_from_db = Choice.objects.get(id=choice.id)
        
        self.assertEqual(first=choice.choice_text,
                         second=choice_from_db.choice_text)
        self.assertEqual(first=choice.votes,
                         second=choice_from_db.votes)
        self.assertEqual(first=question.id,
                         second=choice_from_db.question.id)
        self.assertEqual(first=question.question_text,
                         second=choice_from_db.question.question_text)
        self.assertEqual(first=question.pub_date,
                         second=choice_from_db.question.pub_date)

    def test_choice_str(self):
        """Test that the choice str return the correct id and
            limit the text length to 30 chars.
        """
        choice_str = "Choice 3003, 1234567890 1234567890 12345678"
        self.assertEqual(first=choice_str, second=self.test_choice_1.__str__())

    def test_empty_choices(self):
        """Test for empty choices. The page should show a message
            like "no choices".
        """
        question = Question.objects.create(
                        question_text = "test question 1",
                        pub_date = datetime(year=2024, month=1, day=1),
                    )
        # The question does not have any choices.
        # When the question_detail is shown, there choices will be empty.
        page_url = reverse("polls:question_detail", 
                           kwargs={"question_id": question.id})
        response = self.client.get(path=page_url)
        self.assertEqual(first=200, second=response.status_code)
        question_from_response = response.context["question"]
        # validate the question is the test question
        self.assertEqual(question, question_from_response)
        # validate that the query set for choice is empty
        self.assertQuerySetEqual(question_from_response.choice_set.all(), [])
        
    def test_choice_view(self):
        """Test for empty choices. The page should show a message
            like "no choices".
        """
        question = Question.objects.create(
                        question_text = "test question 1",
                        pub_date = datetime(year=2024, month=1, day=1),
                    )
        choice_1 = Choice.objects.create(
            choice_text = "test choice 1",
            votes = 0,
            question = question
        )
        choice_2 = Choice.objects.create(
            choice_text = "test choice 2",
            votes = 0,
            question = question
        )
        page_url = reverse("polls:question_detail", 
                           kwargs={"question_id": question.id})
        response = self.client.get(path=page_url)
        self.assertEqual(first=200, second=response.status_code)
        question_from_response = response.context["question"]
        # validate the question is the test question
        self.assertEqual(question, question_from_response)
        # validate that the query set for choice is empty
        choice_from_response_1 = response.context["question"].choice_set.get(id=choice_1.id)
        self.assertEqual(choice_from_response_1.choice_text, choice_1.choice_text)
        choice_from_response_2 = response.context["question"].choice_set.get(id=choice_2.id)
        self.assertEqual(choice_from_response_2.choice_text, choice_2.choice_text)
        

