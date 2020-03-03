from django.shortcuts import render

from django.http import HttpResponse
from .models import Question
import requests
from bs4 import BeautifulSoup as soup
import lxml
import datetime
from django.utils.timezone import utc

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

    menu = soup(d.text,'html.parser')
    meals = menu.findAll('td')
    T = []
    for e in meals:
        T.append(str(e)[4:-5])

    context = {'T':T}
    return render(request,'polls/food.html',context)

def swim(request):
    session = requests.Session() #otwarcie połączenia dla cityzen
    content = session.get('https://basen-cityzen-cms.efitness.com.pl/kalendarz-zajec') #pobranie zawartosci strony
    cityzen_site = soup(content.text,'html.parser')

    day = cityzen_site.findAll('a',class_="scheduler-go-to-day") #sprawdzenie dnia tygodnia
    day = str(day)
    day = soup(day,'lxml')
    day = day.text
    day = day[1:-1]

    now = datetime.datetime.utcnow().replace(tzinfo=utc)#sprawdzenie aktualnego czasu
    now = datetime.datetime.now().strftime('%H:%M')
    hour = now
    #session.config['keep_alive'] = False
    #session2 = requests.Session()#otwarcie poł dla POSIRu
    #content2 = session2.get('https://basen-cityzen-cms.efitness.com.pl/kalendarz-zajec') #pobranie zawartosci strony
    #posir_site = soup(content2.text,'html.parser')
    tory = cityzen_site.findAll('td')
    tor2 = tory[85].get_text()




    T = []
    for i in range(len(tory)):
        T.append(tory[i].get_text().strip())

    a = T[T.index('05:45'):T.index('06:30')-1].count('')    #-1 przy indeksach ignoruje mały basen
    b = T[T.index('06:30'):T.index('07:15')-1].count('')
    c = T[T.index('07:15'):T.index('08:00')-1].count('')
    d = T[T.index('08:00'):T.index('08:45')-1].count('')
    e = T[T.index('08:45'):T.index('09:30')-1].count('')
    f = T[T.index('09:30'):T.index('06:30')-1].count('')
    g = T[T.index('05:45'):T.index('10:15')-1].count('')
    h = T[T.index('10:15'):T.index('11:00')-1].count('')
    i = T[T.index('11:00'):T.index('11:45')-1].count('')
    j = T[T.index('11:45'):T.index('12:30')-1].count('')
    k = T[T.index('12:30'):T.index('13:15')-1].count('')
    l = T[T.index('13:15'):T.index('14:00')-1].count('')
    m = T[T.index('14:00'):T.index('14:45')-1].count('')
    n = T[T.index('14:45'):T.index('15:30')-1].count('')
    o = T[T.index('15:30'):T.index('16:15')-1].count('')
    p = T[T.index('16:15'):T.index('17:00')-1].count('')
    r = T[T.index('17:00'):T.index('17:45')-1].count('')
    s = T[T.index('17:45'):T.index('18:30')-1].count('')
    t = T[T.index('18:30'):T.index('19:15')-1].count('')
    u = T[T.index('19:15'):T.index('20:00')-1].count('')
    w = T[T.index('20:00'):T.index('20:45')-1].count('')
    x = T[T.index('20:45'):T.index('21:30')-1].count('')
    y = T[T.index('21:30'):len(T)-1].count('')
    p = y
    tor

    context = {'day':day,'hour':hour,'tor2':tor2,'p':p,'T':T}
    return render(request,'polls/swim.html',context)
