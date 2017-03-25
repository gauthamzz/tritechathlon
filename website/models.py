from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Ranking(models.Model):
    username=models.CharField(max_length=100,primary_key=True)
    score=models.IntegerField()
    timestarted=models.DateTimeField(auto_now=True,auto_now_add=False)

    def __unicode__(self):
        return unicode(self.username)

    def __str__(self):
        return self.username