from django.db import models

class Stadup(models.Model):
    group = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    done = models.TextField(default='')
    todo = models.TextField(default='')
    problems = models.TextField(default='')
    publication = models.DateTimeField(auto_now_add=True)


class Smile(models.Model):
    group = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    before = models.TextField(default='')
    after = models.TextField(default='')
    publication = models.DateTimeField(auto_now_add=True)