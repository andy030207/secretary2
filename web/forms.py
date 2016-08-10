# -*- coding: UTF-8 -*-
from django import forms
from web.models import Diary

# 日誌表單
class DiaryForm(forms.ModelForm):
        class Meta:
                model = Diary
                fields = ['memo']