from django.shortcuts import render
from django.http import JsonResponse
from paser import parsetest as pt


# Create your views here.
def post_list(request):
    data = [
        {
            'id': 2014104154,
            'title': 'Operating System',
            'content': 'Practice_01',
            'duedate': '2018.09.19 08:00 - 2018.12.31 23:50',
            'submit': 'N'
        }
    ]
    data.append(pt())
    return JsonResponse(data, safe=False)


def board(request):
    data = [
        {
            'subject': 'BigDataProgramming',
            'author': 'JinHo',
            'date': '2018.09.19 17:52',
            'content': 'Big Data num mo jae mi it Da!'
        }
    ]
    return JsonResponse(data, safe=False)


def login(request):
    # TODO request.id , request.password 같은 식으로 로그인 처리
    pass
