from django.db import models


# Create your models here.


class Course(models.Model):
    class_code = models.CharField(max_length=20)  # 강의코드
    class_name = models.CharField(max_length=20)  # 강의명
    instructor = models.CharField(max_length=20)  # 강사명


class CoursePost(models.Model):
    title = models.CharField(max_length=100)  # 게시물 제목
    class_code = models.CharField(max_length=20)  # 속한 강의 코드
    content = models.TextField()  # 게시물 내용
    author_id = models.CharField(max_length=20)  # 작성자
    create_date = models.DateTimeField(auto_now_add=True)  # 생성시간
    update_date = models.DateTimeField(auto_now=True)  # 갱신 시간
    hit = models.IntegerField()  # 조회수


class User(models.Model):
    student_id = models.CharField(max_length=20)  # 학번
    pw = models.CharField(max_length=20)  # 비밀번호
    naver_id = models.CharField(max_length=20)  # 클로바 연동용 네이버 아이디
    # 과목 리스트
    #
    #

