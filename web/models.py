# -*- coding: UTF-8 -*-
from django.db import models

# 日誌
class Diary(models.Model):
        memo = models.TextField()
        time = models.DateTimeField(auto_now_add=True)
        def __unicode__(self):
                return self.memo

# 月份
class Month(models.Model):
        date = models.IntegerField(default=0)