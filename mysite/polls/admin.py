from django.contrib import admin
# Register your models here.
from .models import Question, Choice
from django.contrib import admin
from .models import Choice, Question


#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date']}),
#    ]
#    
#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']
#
#admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)

#admin.site.register(Question)

