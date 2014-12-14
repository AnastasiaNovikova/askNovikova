# coding=utf-8
from random import randint
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from askMe.models import Question, Answer, Tag


class Command(BaseCommand):

    def handle(self, *args, **options):

        user_list = User.objects.all()
        len(user_list)

        #for i in range(0, 100):
        #    t = Tag()
        #    t.tag = u'Тег' + str(i)
        #    t.save()

        tag_list = Tag.objects.all()
        len(tag_list)

        for i in range(0, 100000):
            user_id = randint(0, 10000)
            try:
                user = user_list.get(pk=user_id)
            except User.DoesNotExist:
                user = user_list.get(pk=1)
            q = Question()
            q.author = user
            q.title = u'Вопрос №' + str(i)
            q.content = u'Очень длинное и интереесное, а так же непонятное содержание вопроса  №' + str(i)
            q.save()

            tag_count = randint(0, 100)

            for j in range(1, tag_count):
                try:
                    t = tag_list.get(pk=j)
                except Tag.DoesNotExist:
                    t = tag_list.get(pk=1)
                q.tag_set.add(t)
            #q.save()

        q_list = Question.objects.all()
        len(q_list)
        for i in range(76321, 1000000):

            user_id = randint(0, 10000)
            try:
                user = user_list.get(pk=user_id)
            except User.DoesNotExist:
                user = user_list.get(pk=1)

            q_id = randint(0, 100000)
            try:
                q = q_list.get(pk=q_id)
            except Question.DoesNotExist:
                q = q_list.get(pk=1)

            a = Answer()
            a.author = user
            a.question = q
            a.content = u'Гениальный ответ на не менее гениальный вопрос =)'
            if i % 5 == 0:
                a.flag = True
            a.save()