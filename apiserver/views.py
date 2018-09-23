from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from paser import parsetest as pt
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def login(request):
    # TODO 저장된 데이터로 크롤링 시도 후 로그인 성공했으면 1 실패했으면 0
    if request.method == 'POST':
        # POST 방식으로 key 값 id 와 pw 로 받은 데이터를 저장
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print(id, pw)
        # 저장된 데이터로 크롤링 시도 후 로그인 성공했으면 1 실패했으면 0
        # flag = crawling(id,pw)
        # return HttpResponse(flag)
    else:
        print(request.body)
    return HttpResponse('test')


@csrf_exempt
def getassignment(request):
    # 학번 비밀번호 받아서 과제/싸강 긁어오기
    if request.method == 'POST':
        # POST 방식으로 key 값 id 와 pw 로 받은 데이터를 저장
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print(id, pw)
        # TODO 저장된 데이터로 현재 로그인된 사용자의 과제 정보와 제출여부를 json 으로 반환

    else:
        print(request.body)
    return HttpResponse('test')
