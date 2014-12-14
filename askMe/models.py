# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=256,  verbose_name=u'Заголовок')
    content = models.TextField(verbose_name=u'Текст вопроса')
    adding_date = models.DateField(auto_now_add=True, verbose_name=u'Дата создания')
    author = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    content = models.TextField(verbose_name=u'Текст ответа')
    adding_date = models.DateField(auto_now_add=True, verbose_name=u'Дата создания')
    flag = models.BooleanField(default=False, verbose_name=u'Ответ правильный?')
    question = models.ForeignKey('Question')
    author = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return u'Ответ на вопрос: ' + self.question.title


class Tag(models.Model):
    tag = models.CharField(max_length=256,  verbose_name=u'Тег')
    question = models.ManyToManyField('Question', null=True, blank=True)

    def __unicode__(self):
        return self.tag


class Profile(models.Model):
    user = models.OneToOneField(User)

    avatar = models.ImageField(upload_to='/avatars')