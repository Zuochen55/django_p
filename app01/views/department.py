from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import UserModleForm,VipEditModelForm,VipModelForm


# Create your views here.
def department(request):
    depart = models.Department.objects.all()

    return render(request, 'depart_list.html', {"depart": depart})


def add_department(request):
    if request.method == "GET":
        return render(request, "add_department.html")

    title = request.POST.get("title")
    models.Department.objects.create(title=title)

    return redirect("/department/list/")


def delete_department(request):
    nid = request.GET.get('nid')

    models.Department.objects.filter(id=nid).delete()

    return redirect("/department/list/")


def edit_department(request, nid):
    if request.method == "GET":
        row_text = models.Department.objects.filter(id=nid).first()
        print(row_text)
        return render(request, "edit_department.html", {"row_text": row_text})

    title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/department/list/")