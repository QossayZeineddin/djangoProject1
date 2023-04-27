from django.http import HttpResponse
from django.shortcuts import render

from first_applecation.models import Question


# Create your views here.

def index(request ):
    #question_list = Question.objects.order_by("-pub_date")[:5]
    #print(question_list)
    #return HttpResponse("".join( [q.question_text for q in  question_list]))
    return render(request , "normal_user/index.html")
def detail(request , question_id):
    return HttpResponse("you're looking at question %s . " % question_id)

def results(request , question_id):
    response = "you're looking at the results of question %s ."
    return HttpResponse(response % question_id)

def vote(request , question_id):
    return HttpResponse(f"you're voting on question {question_id}.")

