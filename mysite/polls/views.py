from django.shortcuts import render

from django.http import HttpResponse
from .models import Question
import requests
from bs4 import BeautifulSoup as soup

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def menu(request):
    s = requests.Session()
    data = {"login":"331a66", "password":"45gegge457272e"}
    url = "http://honesta.poznan.pl/bursa/"

    r = s.post(url, data=data)
    d = s.get('http://honesta.poznan.pl/bursa//index.php?site=foodmenu')

    menu = soup(d.text)
    meals = menu.findAll('td')
    T = []
    for e in meals:
        T.append(str(e)[4:-5])

    context = {'T':T}
    return render(request,'polls/food.html',context)
