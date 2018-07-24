# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateTimeField()

    def __str__(self):
        return "BookInfo的ID是：%d".encode('utf-8') % self.pk


class HeroInfo(models.Model):
    hanme = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey('BookInfo')
