from django.contrib import admin
from .models import Blog, Tag, Category
# Register your models here.

'''
class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class TagInline(admin.TabularInline):
    model = Tag
'''


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', ]
    list_filter = ['created_time', 'modified_time']
    ordering = ('-modified_time', '-created_time', )
    search_fields = ['content', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ('name', )
    search_fields = ['name', ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ('name', )
    search_fields = ['name', ]
 