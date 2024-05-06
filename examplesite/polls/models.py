import datetime
from xmlrpc.client import boolean

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Question(models.Model):
    """
    A class representing a question in the poll.

    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime): The date and time when the question was published.

    Methods:
        __str__(): Returns a string representation of the question.
        was_published_recently(): Checks if the question was published recently.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        """
        Returns a string representation of the question.

        Returns:
            str: The text of the question.
        """
        return self.question_text
    
    @admin.display(
                    boolean=True,
                    ordering="pub_date",
                    description="Published recently?",
            )
    
    def was_published_recently(self):
        """
        Checks if the question was published recently.

        Returns:
            bool: True if the question was published within the last day, False otherwise.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    

class Choice(models.Model):
    """
    A class representing a choice for a question in the poll.

    Attributes:
        question (Question): The question to which the choice belongs.
        choice_text (str): The text of the choice.
        votes (int): The number of votes received by the choice.

    Methods:
        __str__(): Returns a string representation of the choice.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        """
        Returns a string representation of the choice.

        Returns:
            str: The text of the choice.
        """
        return self.choice_text