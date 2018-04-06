from django.shortcuts import render
from . import models
from django.db.models import Count


def blog_list(request):
    context = {}
    blogs = models.Blog.objects.all().order_by('-created_time')
    categories = models.Category.objects.annotate(blog_num=Count(
        'blog')).filter(blog_num__gt=0).order_by('-blog_num')[:8]
    tags = models.Tag.objects.annotate(blog_num=Count('blog')).filter(
        blog_num__gt=0).order_by('-blog_num')[:32]
    dates = models.Blog.objects.dates(
        'created_time', 'month', order='DESC')[:8]
    context['blogs'] = blogs
    context['categories'] = categories
    context['dates'] = dates
    context['tags'] = tags
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, blog_pk):
    pass
