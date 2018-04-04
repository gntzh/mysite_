from django.db import models
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('问题', max_length=200)
    pub_date = models.DateTimeField('发布时间')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近发布?'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name='问题')
    choice_text = models.CharField('选项', max_length=200)
    votes = models.IntegerField('票数', default=0)

    def __str__(self):
        return self.choice_text
