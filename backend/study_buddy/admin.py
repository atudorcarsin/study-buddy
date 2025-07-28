from django.contrib import admin

from .models import Module, Item, Quiz, Summary, Flashcard
# Register your models here.

admin.site.register(Module)
admin.site.register(Item)
admin.site.register(Quiz)
admin.site.register(Summary)
admin.site.register(Flashcard)
