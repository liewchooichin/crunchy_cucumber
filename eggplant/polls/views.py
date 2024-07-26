from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# using F() to query database
from django.db.models import F
# Create your views here.
from polls.models import Question, Choice

def index(request):
    """Polls homepage"""
    template = loader.get_template("polls/index.html")
    context = {
        "title": "Home"
    }
    return HttpResponse(template.render(context, request))

def question_list_recent(request, recent=None):
    """List of questions"""
    # check for display all question or only recent question
    print(f"\t{request=}")
    print(f"\t{request.POST.get('recent')=}")
    # latest question only
    # request.POST.get('recent')='1'
    if request.POST.get("recent") == "on":
        latest_question_list = Question.objects.order_by("-pub_date")[:2]
    else:
        # request.POST.get('recent')=None
        # all questions
        latest_question_list = Question.objects.order_by("-pub_date")
    
    template = loader.get_template("polls/question_list_recent.html")
 
    context = {
        "title": "Question list",
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def question_list(request, recent=None):
    """List of questions"""
    # all questions
    latest_question_list = Question.objects.order_by("-pub_date")
    
    template = loader.get_template("polls/question_list.html")
    context = {
        "title": "Question list",
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def question_detail(request, question_id):
    """Detail of a question"""
    question = get_object_or_404(Question, id=question_id)
    template = loader.get_template("polls/question_detail.html")
    context = {
        "title": "Question detail",
        "question": question,
    }
    return HttpResponse(template.render(context, request))


def question_vote(request, question_id):
    """Vote for a question, similar to detail of a question.
       But this view has a vote button.
    """
    question = get_object_or_404(Question, id=question_id)
    template = loader.get_template("polls/question_vote.html")
    context = {
        "title": "Question vote",
        "question": question,
    }
    return HttpResponse(template.render(context, request))


def vote(request, question_id):
    """User click on the vote button to vote"""
    question = get_object_or_404(Question, id=question_id)
    try:
        # Get the user's choices
        selected_choice = question.choice_set.get(
            id=request.POST["choice"]
        )
        #print(f"\t{selected_choice=}")
    except(KeyError, Choice.DoesNotExist): 
        # Mapping key not found
        # Redisplay the question voting form
        return render(request=request,
                      template_name="polls/question_vote.html",
                      context = {
                           "title": "Voting",
                           "question": question,
                           "error_message": "You did not select a choice."
                      })
    else:
        # Using F() to directly use the database query
        print(f"\tIn vote: current votes: {selected_choice.votes}")
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # After save, we have to retrieve the object again to get
        # the latest state of the db.
        selected_choice = Choice.objects.get(id=selected_choice.id)
        print(f"\tIn vote: after votes: {selected_choice.votes}")
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(
        #     reverse("polls:results", args=(question.id,))
        # )
        return HttpResponseRedirect(
            reverse("polls:vote_results", args=(question.id, ))
        )


def vote_results(request, question_id):
    """Display the results of a vote"""
    question = get_object_or_404(Question, id=question_id)
    context = {
        "title": "Results",
        "question": question,
    }
    return render(request=request, 
                  template_name="polls/vote_results.html",
                  context=context)


# HTMX tutorial
def question_list_htmx(request):
    """Display question using htmx"""
    context = {"title": "List HTMX" }
    return render(request=request, 
                  template_name="polls/question_list_htmx.html", 
                  context=context)

import time
def question_partial(request):
    """Partial question to be loaded by HTMX"""
    time.sleep(2) # 2 sec: to simulate lazy loading
    context = {
        "title": "Partial questions",
        "questions": Question.objects.all(),
    }
    return render(request=request,
                  template_name="polls/partials/question_list_partial.html",
                  context=context
                )


def choices_partial(request, question_id):
    """Display detail of question using htmx"""
    context = {
        "some_text": question_id,
    }
    return render(request=request,
                  template_name="polls/partials/choices_partial.html",
                  context=context)

# For searching questions
from django.db.models import Q
import urllib

def search_results(request):
    """Search question from the keywords given by users"""
    search_text = request.GET.get("search_text", "")
    # A URL param was encoded. Turn it back into a regular
    # string.
    search_text = urllib.parse.unquote(search_text)
    # make lowercase for case insensitive search
    search_text = search_text.lower() 
    search_text = search_text.strip()

    results = []

    if search_text:
        # split the text into individual terms
        parts = search_text.split()
        print(f"\t{parts=}")
        # Build a Q objects OR-ed together to search
        # for this term in the questions
        # build the first query term
        q = Q(question_text__icontains=parts[0])
        print(f"\t{q=}")
        # if there are more than one search terms
        if len(parts) > 1:
            for x in parts[1:]:
                print(f"\t{x=}")
                q |= Q(question_text__icontains=x)
        # Search the Question filter with the query 
        # built with Q.
        results = Question.objects.filter(q)
    
    # compose the context
    context = {
        "title": "Search results",
        "search_text": search_text,
        "results": results
    }
    return render(request=request, template_name="polls/search_results.html",
                  context=context)