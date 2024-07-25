from django.test import TestCase

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
        self.test_choice = Choice.objects.create(
            id=3003, # an unlikely id
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
        self.assertEqual(first=choice_str, second=self.test_choice.__str__())

