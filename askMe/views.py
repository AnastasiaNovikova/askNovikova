from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Question, Tag
from django.contrib.auth import logout

import datetime
# Create your views here.
def index(request):
    q_list = Question.objects.select_related('author', 'author__profile').order_by('-adding_date')[:5]
    tag_list = Tag.objects.annotate(num_questions=Count('question')).order_by('-num_questions')[:15]
    author_list = User.objects.annotate(num_questions=Count('answer')).order_by('-num_questions')[:15]

    context = {}
    context['text'] = 'Hello world'
    context['latestQuestions'] = q_list
    context['popularTags'] = tag_list
    context['bestMembers'] = author_list
    return render(request, 'askMe/index.html', context)

def signup(request):
    context = {}
    return render(request, 'askMe/signup.html', context)

def login(request):
    q_list = Question.objects.select_related('author', 'author__profile').order_by('-adding_date')[:5]
    tag_list = Tag.objects.annotate(num_questions=Count('question')).order_by('-num_questions')[:15]
    author_list = User.objects.annotate(num_questions=Count('answer')).order_by('-num_questions')[:15]

    context = {}
    context['popularTags'] = tag_list
    context['bestMembers'] = author_list

    return render(request, 'askMe/login.html', context)

def settings(request):
    tag_list = Tag.objects.annotate(num_questions=Count('question')).order_by('-num_questions')[:15]
    author_list = User.objects.annotate(num_questions=Count('answer')).order_by('-num_questions')[:15]

    context = {}
    context['popularTags'] = tag_list
    context['bestMembers'] = author_list
    return render(request, 'askMe/profile.html', context)