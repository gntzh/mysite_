from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title = models.CharField('标题', max_length=32)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='作者')
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('最近修改', auto_now=True)
    category = models.ForeignKey(
        'Category', on_delete=models.DO_NOTHING, verbose_name='分类')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签')
    content = models.TextField('内容')

    class Meta:
        ordering = [
            '-modified_time',
            '-created_time',
        ]
        verbose_name = '博文'
        verbose_name_plural = '博文'

    def __str__(self):
        return self.title[:16]


class Tag(models.Model):
    name = models.CharField('名称', max_length=16)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name[:8]


class Category(models.Model):
    name = models.CharField('名称', max_length=32)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.name[:16]
