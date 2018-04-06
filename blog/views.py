from django.shortcuts import render, get_object_or_404
from . import models
from django.db.models import Count
from . import z_tools


def blog_list(request):
    context = {}
    blogs = models.Blog.objects.all().order_by('-created_time')
    categories = models.Category.objects.annotate(blog_num=Count(
        'blog')).filter(blog_num__gt=0).order_by('-blog_num')[:8]
    tags = models.Tag.objects.annotate(blog_num=Count('blog')).filter(
        blog_num__gt=0).order_by('-blog_num')[:16]
    dates = models.Blog.objects.dates(
        'created_time', 'month', order='DESC')[:8]
    context['blogs'] = blogs
    context['categories'] = categories
    context['dates'] = dates
    context['tags'] = tags
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, blog_pk):
    blog = get_object_or_404(models.Blog, pk=blog_pk)
    blog.content = z_tools.md.convert(blog.content)
    blog.toc = z_tools.md.toc
    context = {}
    context['blog'] = blog
    return render(request, 'blog/blog_detail.html', context)
