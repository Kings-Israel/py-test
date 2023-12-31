from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_data"]}),
    ]
    inlines = [ChoiceInLine]
    list_display = ["question_text", "pub_data", "was_published_recently"]
    list_filter = ["pub_data"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
