import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    @classmethod
    def get_questions_after_2022(cls):
        return cls.objects.filter(pub_date__year__gt=2022)

    @classmethod
    def questions_between_years(cls):
        """Return the questions with pub_date between 2016 and 2023."""
        start_date = datetime.datetime(2016, 1, 1, tzinfo=timezone.utc)
        end_date = datetime.datetime(2023, 12, 31, tzinfo=timezone.utc)
        return cls.objects.filter(pub_date__range=(start_date, end_date)).order_by('-pub_date')

    @classmethod
    def get_questions_with_high_votes(cls, threshold):
        """Return questions that have choices with votes greater than or equal to the given threshold."""
        question_ids = Choice.objects.filter(votes__gte=threshold).values_list('question_id', flat=True)
        #The values_list method returns a QuerySet containing tuples of values
        return cls.objects.filter(id__in=question_ids)

class Choice(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def get_question(self):
        return self.question

    @classmethod
    def get_choices_with_high_votes(cls, threshold):
        """Return choices with votes greater than or equal to the given threshold."""
        return cls.objects.filter(votes__gte=threshold)