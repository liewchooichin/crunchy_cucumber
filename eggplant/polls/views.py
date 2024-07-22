from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader

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
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404(f"Question {question_id} does not exist")
    template = loader.get_template("polls/question_detail.html")
    context = {
        "title": "Question detail",
        "question": question,
    }
    return HttpResponse(template.render(context, request))


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")