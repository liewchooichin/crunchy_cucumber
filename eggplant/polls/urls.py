# polls/urls.py

from django.urls import path

from polls import views as polls_views

# Namespace
# Declare the app_name here and also specify the namespace
# in the urls of the include() file.
app_name = "polls"

# URLs
urlpatterns = [
     # homepage: /polls/
     path("", polls_views.index, 
         name="index"),
     # display list the questions
     path("question_list/", polls_views.question_list,
          name="question_list"),
     # detail of question: /polls/5
     path("question_detail/<int:question_id>/", 
          polls_views.question_detail, 
         name="question_detail"),
     # vote for a question, display the detail of a question
     path("question_vote/<int:question_id>/",
          polls_views.question_vote,
          name="question_vote"),
     # vote on a question: /<int:question_id>/vote/
     # this is used in the from action="polls:vote question.id"
     path("<int:question_id>/vote/", polls_views.vote, 
         name="vote"),
     # results of a question: /<int:question_id>/results/
     path("<int:question_id>/vote_results/", polls_views.vote_results, 
         name="vote_results"),
]