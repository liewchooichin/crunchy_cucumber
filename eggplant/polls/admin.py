from django.contrib import admin

# Register your models here.
from .models import Question, Choice


# Choices of inlines are:
# admin.StackedInline
# admin.TabularInline
class ChoiceInline(admin.TabularInline):
    """Create choices in the question page"""
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """Create question and choices together in one page"""
    # split the form into fieldsets
    # fields: cannot use the method as a field. That is the fields cannot include
    # was_published_recently.
    # list_display: can include the method was_published_recently.
    # list_display is the list of all questions.
    # fieldsets are in the individual question.
    fieldsets = [
        ("Questions", 
         {
             "fields": ["question_text"], 
             "description": "The question."}
         ),
        ("Date information", 
            {
                "fields": ["pub_date"],
                "classes": ["collapse"],
                "description": "When the question is created"
            }
        )
    ]
    list_display = ["question_text", "was_published_recently", "pub_date" ]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)