from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


@admin.register(Question)
class Questiondmin(admin.ModelAdmin):
    list_display = (
        'id',
        'question_text',
        'was_published_recently',
    )
    ordering = ("pub_date", )
    fieldsets = [
        (None, {
            'fields': ['question_text']
        }),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ['collapse']
        }),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']


'''
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'votes', )
    ordering = ('votes',)
'''
