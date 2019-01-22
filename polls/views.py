from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse('detail. Question id: {} Question: {}'.format(question_id, question.question_text))


def results(request, question_id):
    return HttpResponse('results. Question id: {}'.format(question_id))


def vote(request, question_id):
    return HttpResponse('vote. Question id: {}'.format(question_id))

@ensure_csrf_cookie
def crate_new_user(request):
    name = request['username']
    password = request['pass']
    user = User.objects.create_user(name, 'sanya@mail.ru', password)
    user.save()


def show_users(requset):
    users = User.objects.all()
    output = '\n'.join([user.username for user in users])
    return HttpResponse(output)