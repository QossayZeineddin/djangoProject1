from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from first_applecation.models import Question,Choise


# Create your views here.

def index(request ):
    question_list = Question.objects.order_by("-pub_date")[:5]
    #print(question_list)
    #return HttpResponse("".join( [q.question_text for q in  question_list]))
    context = {"question_list" : question_list }
    return render(request , "normal_user/index.html" , context)
def detail(request , question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "normal_user/detail.html" , {"question" :question })

def results(request , question_id , question_name =''):
    #response = f"you're looking at the results of question {question_id}  .  {question_name}"
    question = get_object_or_404(Question , pk = question_id)
    return render(request , 'normal_user/results.html' , {"question": question})

def vote(request , question_id):
    question = get_object_or_404(Question , pk = question_id)
    try:
        selected_choice = question.choise_set.get(pk = request.POST["choise"])
        print("dddd")
    except(KeyError, Choise.DoesNotExist):
        print("gggg")
        return render(request ,'normal_user/detail.html' ,{"question" : question , "error_message" : "You didn't select a choice ???."} )

    else:
        print("fdfdfdfd")
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results' , args=(question.id,)))


