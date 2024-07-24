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

    def test_choice_str(self):
        """Test that the choice str return the correct id and
            limit the text length to 30 chars.
        """
        choice_str = "Choice 3003, 1234567890 1234567890 12345678"
        self.assertEqual(first=choice_str, second=self.test_choice.__str__())

