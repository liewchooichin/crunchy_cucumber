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
        self.test_1 = Question.objects.create(
            question_text = "Where can the tallest tree be found?",
            pub_date = datetime(year=2024, month=10, day=10)
        )
        self.test_2 = Question.objects.create(
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
  
    def test_search_results_0(self):
        """Test search with no results
            Search flower is not in the Question.
        """
        page_url = reverse("polls:search_results")
        response = self.client.get(page_url)
        # get data to the search page
        data = {"search_text": "flower"}
        response = self.client.get(path=page_url, data=data)
        # print(f"\tResponse{response}")
        self.assertEqual(first=200,
                         second=response.status_code,
                         msg="Successfully call search_results")
        # check the results in the response,
        # there should be no result.
        results = response.context["results"]
        # print(f"\tLen of results: {len(results)}")
        self.assertQuerySetEqual(qs=results, values=[])
        
    def test_search_results_1(self):
        """Test the search with two results.
            Search tree OR tallest will give two results.
        """
        page_url = reverse("polls:search_results")
        # get data to the search page
        # It is not necessary to quote the query string in test.
        # The Client.get will do the necessary work for the query string.
        #search_text = urllib.parse.quote_plus("tree", encoding='utf-8')
        search_text = "tree tallest"
        # print(f"\tQuoted search text: {search_text}")
        data = {"search_text": search_text}
        response = self.client.get(path=page_url, data=data)
        self.assertEqual(first=200,
                         second=response.status_code,
                         msg="Successfully call search_results")
        # check the results in the response,
        # there should be no result.
        # print(f"\tRequest: {response.request}")
        # print(f"\tSearch text: {response.context['search_text']}")
        # print(f"\tResults: {response.context['results']}")
        # print(f"\tLen of results: {len(response.context['results'])}")
        self.assertQuerySetEqual(qs=response.context["results"], 
                             values=[self.test_1, self.test_2])

    def test_search_results_2(self):
        """Test the search with two results.
            Search animal OR tallest will give two results.
        """
        page_url = reverse("polls:search_results")
        search_text = "animal tallest"
        # print(f"\tQuoted search text: {search_text}")
        data = {"search_text": search_text}
        response = self.client.get(path=page_url, data=data)
        self.assertEqual(first=200,
                         second=response.status_code,)
        # check the results in the response,
        # there should be 2 result.
        # print(f"\tRequest: {response.request}")
        # print(f"\tSearch text: {response.context['search_text']}")
        # print(f"\tResults: {response.context['results']}")
        # print(f"\tLen of results: {len(response.context['results'])}")
        self.assertQuerySetEqual(qs=response.context["results"], 
                             values=[self.test_1, self.test_2],)

    def test_search_results_3(self):
        """Test the search with one result.
            Search animal will give one result.
        """
        page_url = reverse("polls:search_results")
        # It is not necessary to quote the query string in test.
        # The Client.get will do the necessary work for the query string.
        #search_text = urllib.parse.quote_plus("tree", encoding='utf-8')
        search_text = "animal"
        # print(f"\tQuoted search text: {search_text}")
        data = {"search_text": search_text}
        response = self.client.get(path=page_url, data=data)
        self.assertEqual(first=200,
                         second=response.status_code,
                         msg="Successfully call search_results")
        # check the results in the response,
        # there should be no result.
        # print(f"\tRequest: {response.request}")
        # print(f"\tSearch text: {response.context['search_text']}")
        # print(f"\tResults: {response.context['results']}")
        # print(f"\tLen of results: {len(response.context['results'])}")
        self.assertQuerySetEqual(qs=response.context["results"], 
                                 values=[self.test_2],)