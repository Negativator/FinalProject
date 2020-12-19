from django.contrib import admin
from .models import Quiz, Section, Question, QuestionMC, QuestionSA

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(QuestionMC)
admin.site.register(QuestionSA)