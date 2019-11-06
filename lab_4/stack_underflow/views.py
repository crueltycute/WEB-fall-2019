from django.shortcuts import render
import random

DATA = [{'id': 0, 'votes': -12, 'answers': random.randint(0, 20)},
        {'id': 1,  'votes': 37, 'answers': random.randint(0, 20)},
        {'id': 2,  'votes': 129, 'answers': random.randint(0, 20)},
        {'id': 3,  'votes': 0, 'answers': random.randint(0, 20)},
        {'id': 4,  'votes': 15, 'answers': random.randint(0, 20)},
        ]


def index(request):
    context = {
        'questions_data': DATA
    }

    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def question(request, question_id):
    question_id = int(question_id)

    context = {
        'question': {'id': DATA[question_id].get('id'),
                     'votes': DATA[question_id].get('votes'),
                     'answers': DATA[question_id].get('answers')}
    }

    return render(request, 'question.html', context)
