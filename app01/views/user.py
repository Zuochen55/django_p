from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import UserModleForm,VipEditModelForm,VipModelForm


# Create your views here.


def user_list(request):
    querySet = models.UserInfo.objects.all()
    page_obj = Pagination(request,querySet,page_size=2,plus=1)
    context = {"querySet": page_obj.page_queryset,
               "page_string": page_obj.html()
    }

    return render(request, 'user_list.html', context)


def user_add(request):
    if request.method == "GET":
        form = UserModleForm()
        return render(request, "user_add.html", {"form": form})

    form = UserModleForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")

    return render(request, "user_add.html", {"form": form})


def user_edit(request, nid):
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModleForm(instance=row_object)
        return render(request, "user_edit.html", {"form": form})

    form = UserModleForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")

    return render(request, "user_edit.html", {"form": form})


def user_delete(request):
    nid = request.GET.get("nid")
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")