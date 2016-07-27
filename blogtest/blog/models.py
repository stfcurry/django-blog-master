from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class Title(models.Model):
    title = models.CharField(max_length=150)
    def __unicode__(self):
        return self.title

class All(models.Model):
    title = models.ForeignKey(Title)
    name = models.CharField(max_length=150)
    body = models.TextField()
    def __unicode__(self):
        return self.name

class TitleAdmin(admin.ModelAdmin):
    list_display = ('title',)

class AllAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Title,TitleAdmin)
admin.site.register(All,AllAdmin)
