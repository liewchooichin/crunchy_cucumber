from django.db import models

# other libraries
from datetime import date, datetime, timedelta

# app libraries

# Create your models here.



# A Question has a question and a publication date. 
# A Choice has two fields: the text of the choice 
# and a vote tally. 
# Each Choice is associated with a Question.
class Question(models.Model):
    """Question model"""
    id = models.SmallAutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name="date published")
    
    def was_published_recently(self) -> bool:
        """Whether the publication date is recent or not."""
        # Recent is true when the question is published within 7 days,
        # publication date cannot be in future date
        recent = False
        if (
            (datetime.today() - timedelta(days=7)) <= self.pub_date \
              <= datetime.today()
           ):
            recent = True
        return recent

    def __str__(self):
        """Return only up to 30 chars"""
        return f"Question {self.id}, {self.question_text[:30]}"

class Choice(models.Model):
    """Choice model."""
    id = models.SmallAutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return the Choice"""
        return f"Choice {self.id}, {self.choice_text[:30]}"