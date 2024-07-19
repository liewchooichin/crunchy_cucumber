from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Namespace
app_name = "polls"

def index(request):
    """Polls homepage"""
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")