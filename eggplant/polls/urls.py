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
     # display list the questions--all questions
     path("question_list/", polls_views.question_list,
          name="question_list"),
     # display only the latest 5 questions
     path("question_list_recent/", polls_views.question_list_recent,
          name="question_list_recent"),
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
     # htmx pages, use the same question_list view for the 
     # beginning link
     path("question_list_htmx/", polls_views.question_list_htmx,
          name="question_list_htmx"),
     # using htmx to display a question in the top homepage
     path("choices_partial/", polls_views.choices_partial,
          name="choices_partial"),
     # partial question to be loaded into the question list above
     path("question_partial", polls_views.question_partial,
          name="question_partial"),
     # search results
     path("search_results/", polls_views.search_results,
          name="search_results"),
     # click-to-edit
     path("question_list_edit/", polls_views.question_list_edit,
          name="question_list_edit"),
     # form for the click-to-edit
     path("edit_question_form/<int:question_id>/", polls_views.edit_question_form,
          name="edit_question_form"),
]