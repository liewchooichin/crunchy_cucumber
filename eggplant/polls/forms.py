# forms for polls app

from django import forms
from polls.models import Question, Choice

class QuestionForm(forms.Form):
    model = Question
    fields = ["question_text"]