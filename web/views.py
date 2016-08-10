# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from models import Diary, Month
from forms import DiaryForm
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.utils.timezone import localtime

# 瀏覽日誌
def diary(request):
        diaries = Diary.objects.all().order_by("-id")
        return render_to_response('diary.html', {'diaries': diaries}, context_instance=RequestContext(request))
def diary_add(request):
        if request.method == 'POST':
                form = DiaryForm(request.POST)
                if form.is_valid():
                        form.save()
                        year = localtime(timezone.now()).year
                        month =  localtime(timezone.now()).month
                        try:
                                themonth = Month.objects.get(date=year*100+month)
                        except ObjectDoesNotExist:
                                themonth = Month(date=year*100+month)
                                themonth.save()
                        return redirect("/diary")
        else:
                form = DiaryForm()
        return render_to_response('form.html',{'form': form}, context_instance=RequestContext(request))
    