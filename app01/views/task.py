from django.shortcuts import render,redirect,HttpResponse
from app01.utils.bootstrap import BootstrapModelForm
from django import forms
from app01 import models
from django.views.decorators.csrf import csrf_exempt
import json
from app01.utils.pagination import Pagination

class TaskModelForm(BootstrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets={
            "description":forms.TextInput
        }

def task_list(request):
    form = TaskModelForm()
    queryset = models.Task.objects.all().order_by("-id")
    page_obj = Pagination(request,queryset)

    context = {
        "queryset":page_obj.page_queryset,
        "form":form,
        "page_string":page_obj.html()
    }

    return render(request,"task_list.html",context)

@csrf_exempt
def task_add(request):


    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, "error": form.errors}
    return HttpResponse(json.dumps(data_dict,ensure_ascii=False))