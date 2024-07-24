from django.test import TestCase
from django.urls import reverse

from datetime import datetime, timedelta
from polls.models import Question, Choice

# Create your tests here.

class TestQuestionVote(TestCase):
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
            votes=10,
            question=self.test_question, # point to the question
        )
        # method 2
        self.test_question.choice_set.create(
            choice_text="Choice 2", votes=20
        )
    def tearDown(self):
        pass

    def test_question_vote_view(self):
        """Test the question voting page"""
        page_url = reverse("polls:question_vote", 
                           args=(self.test_question.id, ))
        response = self.client.get(page_url)
        self.assertEqual(first=200, second=response.status_code,
                         msg="Get question voting page")
        # verbose debug
        #print(f"test: {self.test_question}")
        #print(f"first object: {Question.objects.first()}")
        #print(f"last object: {Question.objects.last()}")
        # Validate that the question is in the page
        self.assertIn(member=self.test_question.question_text,
                      container=str(response.content),
                      msg="Test question in voting page")
        # Validate that the choice is in the page
        for item in self.test_question.choice_set.all():
            self.assertIn(member=item.choice_text,
                      container=str(response.content),
                      msg="Test question in voting page")
        # validate non-existing key
        with self.assertRaises(KeyError):
            response.context["non_key"]
        # validate objects does not exists
        response = self.client.get(
                reverse("polls:question_vote", args=(999, ))
            )
        # validate response not found
        response = self.client.get(
                reverse("polls:question_vote", args=(999, ))
            )
        self.assertEqual(first=404, second=response.status_code)
    
    def test_post_to_vote(self):
        # validate the post will redirect to vote_results page
        # get choice #1
        choice_1 = self.test_question.choice_set.get(id=1)
        choice_1_current_count = choice_1.votes
        post_data = {
            "choice": choice_1.id,
        }
        vote_url = reverse(
                "polls:vote", 
                kwargs={"question_id": self.test_question.id}
            )
        # get the page first
        get_response = self.client.get(
            path=vote_url,
        )
        self.assertEqual(first=200, second=get_response.status_code)
        # post the data
        post_response = self.client.post(
            path=vote_url,
            data=post_data,
        )
        # test for response status code 302 for redirection
        self.assertEqual(first=302, second=post_response.status_code)
        #print(f"\t{post_response}")
        # <HttpResponseRedirect status_code=302, "text/html; charset=utf-8",
        #  url="/polls/1/vote_results/">
        # make sure the redirected page is correct
        self.assertRedirects(
            post_response,
            reverse("polls:vote_results", args=(self.test_question.id, )),
        )
        # check that the votes of choice_1 increase by 1
        # After post and save the choice object, we have to retrieve the
        # object again to get the latest db state.
        updated_choice = Choice.objects.get(id=choice_1.id)
        self.assertEqual(first=choice_1_current_count+1,
                         second=updated_choice.votes)
            

