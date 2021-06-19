from django.contrib import admin

admin.site.site_header = "Pollster admin"
admin.site.site_title = "Pollster admin area"
admin.site.index_title = "Welcome"

from .models import Question, Choice
class ChoiceInLine(admin.TabularInline):
    model = Choice 
    extra =2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),('date information', {'fields': ['pub_date']})]
    inlines = [ChoiceInLine]


# Register your models here.

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)