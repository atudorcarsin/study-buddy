from django.contrib import auth
from django.db import models

class Module(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='modules')
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=254, blank=True, null=True)
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='items')
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True, related_name='items')
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=254, blank=True, null=True)
    file_resource = models.FileField(upload_to='items/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='quizzes')
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name='quizzes')
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=254, blank=True, null=True)
    # Multiple Choice Questions
    number_of_mcqs = models.PositiveIntegerField(default=0)
    # True/False Questions
    number_of_tfqs = models.PositiveIntegerField(default=0)
    output = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Summary(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='summaries')
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name='summaries')
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=254, blank=True, null=True)
    has_bullet_points = models.BooleanField(default=False)
    output = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Flashcard(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='flashcards')
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name='flashcards')
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=254, blank=True, null=True)
    output = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name