from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.http import Http404,HttpResponse
from django.urls import reverse
from django.template import loader

# get questions and display them

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

# get specific question and choices

def detail(request , question_id):
        question = get_object_or_404(Question, pk=question_id)
        context = {'question' : question}
        return render(request, 'polls/detail.html', context)

# get question and results

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context= {'question': question}
    return render(request , 'polls/results.html', context)

# vote for a question choice

def vote(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

