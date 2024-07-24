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


def question_list(request):
    """List of questions"""
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
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


