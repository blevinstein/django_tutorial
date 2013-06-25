from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
