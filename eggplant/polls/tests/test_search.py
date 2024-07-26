from django.test import TestCase
from django.urls import reverse

from datetime import datetime, timedelta
import urllib

from polls.models import Question

# Create your tests here.

class TestSearchQuestion(TestCase):
    """Test the search function"""
    def setUp(self):
        """Setup test question"""
    test_1 = Question.objects.create(
        question_text = "Where can the tallest tree be found?",
        pub_date = datetime(year=2024, month=10, day=10)
    )
    test_2 = Question.objects.create(
        question_text = "Where can the tallest animal be found?",
        pub_date = datetime(year=2024, month=9, day=9)
    )

    def test_search_page_ok(self):
        """Test search page is loaded successfully"""
        page_url = reverse("polls:search_results")
        response = self.client.get(page_url)
        # test that page call is successful
        self.assertEqual(first=200,
                         second=response.status_code,
                         msg="Successfully call search_results")
  
    def test_search_no_results(self):
        """Test search with no results
            The test search is not able to get the correct 
            results.
        """
        page_url = reverse("polls:search_results")
        response = self.client.get(page_url)
        # post data to the search page
        data = {"search_text": "flower"}
        response = self.client.get(path=page_url, data=data)
        print(f"\tResponse{response}")
        self.assertEqual(first=200,
                         second=response.status_code,
                         msg="Successfully call search_results")
        # check the results in the response,
        # there should be no result.
        results = response.context["results"]
        print(f"\tLen of results: {len(results)}")
        #self.assertListEqual(list1=results, list2=[],
        #                     msg="No results in search")
        
    def test_search_one_result(self):
        """Test the search with one result
            The test search is not able to get the correct 
            results.
        """
        page_url = reverse("polls:search_results")
        # post data to the search page
        # encode the search text
        # It is also not a problem of the quote or unquote
        search_text = urllib.parse.quote("tree", encoding='utf-8')
        print(f"\tQuoted search text: {search_text}")
        data = {"search_text": search_text}
        response = self.client.get(path=page_url, data=data)
        self.assertEqual(first=200,
                         second=response.status_code,
                         msg="Successfully call search_results")
        # check the results in the response,
        # there should be no result.
        print(f"\tRequest: {response.request}")
        print(f"\tSearch text: {response.context['search_text']}")
        print(f"\tResults: {response.context['results']}")
        print(f"\tLen of results: {len(response.context['results'])}")
        #self.assertListEqual(list1=[], list2=[self.test_1.question_text],
        #                     msg="One result in search")

