from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import UserModleForm,VipEditModelForm,VipModelForm

# Create your views here.


def vipnumber(request):
    data_dict = {}
    value = request.GET.get("q","")
    if value:
        data_dict["mobile__contains"] = value

    queryset = models.VipNumber.objects.filter(**data_dict).order_by("-level")
    pagination = Pagination(request,queryset)

    context = {"queryset": pagination.page_queryset,
               "value":value,
               "page_string":pagination.html()}

    return render(request, "vipnumber.html", context)

def vipnumber_add(request):
    if request.method == "GET":
        form = VipModelForm()
        return render(request, "vipnumber_add.html", {"form": form})

    form = VipModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/vip/number/list/")

    return render(request, "vipnumber_add.html", {"form": form})

def vipnumber_edit(request,nid):
    row_objects = models.VipNumber.objects.filter(id=nid).first()
    if request.method == "GET":
        form = VipEditModelForm(instance=row_objects)
        return render(request, "vipnumber_edit.html", {"form": form})

    form = VipEditModelForm(data=request.POST, instance=row_objects)
    if form.is_valid():
        form.save()
        return redirect("/vip/number/list/")

    return render(request, "vipnumber_edit.html", {"form": form})

def vipnumber_delete(request,nid):
    models.VipNumber.objects.filter(id=nid).delete()
    return redirect("/vip/number/list/")