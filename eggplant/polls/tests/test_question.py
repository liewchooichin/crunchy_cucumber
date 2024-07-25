from django.test import TestCase
from django.urls import reverse

from datetime import datetime, timedelta
from polls.models import Question, Choice

# Create your tests here.

class TestQuestion(TestCase):
    """Test the question of the polls app"""
    def setUp(self):
        """Set up the question test data"""
        self.test_question = Question.objects.create(
            question_text="Test question 1",
            pub_date=datetime.today(),
        )

    def tearDown(self):
        pass

    def test_question_data(self):
        """Test that the test data is what was created
            in the database.
        """
        question = Question.objects.create(
            question_text = "question 1",
            pub_date=datetime(year=2024, month=8, day=1),
        )
        
        question_from_db = Question.objects.get(id=question.id)
        
        self.assertEqual(first=question.question_text,
                         second=question_from_db.question_text)
        self.assertEqual(first=question.pub_date,
                         second=question_from_db.pub_date)

    def test_question_str(self):
        """Test the return str"""
        self.long_question = Question.objects.create(
            # more than 30 chars, the __str__ is supposed to limit
            # the return string to only 30 chars
            id=3003, # an unlikely id
            question_text="1234567890 1234567890 1234567890 1234567890",
            pub_date=datetime.now(),
        )
        print(f"\t{self.long_question}")
        question_str = "Question 3003, 1234567890 1234567890 12345678"
        self.assertEqual(first=question_str, second=self.long_question.__str__())

    def test_published_recently(self):
        """Test the publication date is recent or not"""
        """Create a question that is not recent
            and create a question that is recent
        """
        # this is an old question: false
        self.old_question = Question.objects.create(
            question_text="Old question",
            pub_date=datetime.now()-timedelta(days=7, seconds=1)
        )
        
        print(f"\t{self.old_question.pub_date=}")
        # this is a question with future dates: false
        self.future_question = Question.objects.create(
            question_text="New question",
            pub_date=datetime.now()+timedelta(days=7, seconds=1)
        )
        print(f"\t{self.future_question.pub_date=}")
        # this is a question published within the last day
        self.one_day_old_question = Question.objects.create(
            question_text="One day old question",
            pub_date=datetime.now()-timedelta(hours=23, minutes=59, seconds=59)
        )
        # old question
        self.assertFalse(self.old_question.was_published_recently())
        # question in future date 
        self.assertFalse(self.future_question.was_published_recently())
        # question within the recent test period
        self.assertTrue(self.one_day_old_question.was_published_recently())

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
        # validate the query set in the context is the same
        # as the test question
        self.assertQuerySetEqual(
            qs = response.context["latest_question_list"],
            values = [self.test_question]
        )

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
