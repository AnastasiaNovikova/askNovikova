# coding=utf-8
__author__ = 'anastasia'
from random import randint
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from askMe.models import Question, Answer, Tag

class Command(BaseCommand):

    def handle(self, *args, **options):

        user_list = User.objects.all()
        len(user_list)

        tag_list = Tag.objects.all()
        len(tag_list)

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