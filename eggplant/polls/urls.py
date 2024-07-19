# polls/urls.py

from django.urls import path

from . import views as polls_views

# Namespace
app_name = "polls"

# URLs
urlpatterns = [
    # homepage: /polls/
    path("", polls_views.index, name="polls-index"),
    # detail of question: /polls/5
    path("<int:question_id>/", polls_views.detail, 
         name="polls-detail"),
    # results of a question: /<int:question_id>/results/
    path("<int:question_id>/results/", polls_views.results, 
         name="polls-results"),
    # vote on a question: /<int:question_id>/vote/
    path("<int:question_id>/vote/", polls_views.vote, 
         name="polls-vote"),

]