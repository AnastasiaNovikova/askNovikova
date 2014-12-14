# coding=utf-8
from django.contrib.auth.models import User
from django.core.management import BaseCommand
#from  import Question


class Command(BaseCommand):

    def handle(self, *args, **options):

        for i in range(10, 10000):
            username = u'Пользователь №' + str(i)
            email = u'email' + str(i) + u'@mail.ru'
            u = User.objects.create_user(username, email, 'password')


