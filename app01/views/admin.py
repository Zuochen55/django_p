from django.shortcuts import render,redirect
from app01 import models
from django import forms
from app01.utils.pagination import Pagination
from app01.utils.form import AdminModleForm,AdminEditModleForm,AdminResetModleForm

def admin_list(request):
    queryset = models.Admin.objects.all()
    page_obj = Pagination(request,queryset,page_size=5)
    context = {
        "queryset":page_obj.page_queryset,
        "page_string": page_obj.html()
    }

    return render(request,"admin_list.html",context)



def admin_add(request):
    if request.method == "GET":
        form = AdminModleForm()
        return render(request,"change.html",{"form":form, "title": "Add Admin"})

    form = AdminModleForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect("/admin/list/")

    return render(request,"change.html",{"form":form, "title": "Add Admin"})

def admin_edit(request,nid):
    row_obj = models.Admin.objects.filter(id=nid).first()
    if not row_obj:
        return redirect("/admin/list/")

    if request.method == "GET":
        form = AdminEditModleForm(instance=row_obj)
        return render(request, "change.html", {"form": form, "title": "Edit Admin"})

    form = AdminEditModleForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")

    return render(request, "change.html", {"form": form, "title": "Edit Admin"})

def admin_delete(request,nid):

    models.Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list/")

def admin_reset(request,nid):
    row_obj = models.Admin.objects.filter(id=nid).first()
    if not row_obj:
        return redirect("/admin/list/")

    if request.method == "GET":
        form = AdminResetModleForm(instance=row_obj)
        return render(request, "change.html", {"form": form, "title": "Reset Password - {}".format(row_obj.name)})

    form = AdminResetModleForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")

    return render(request, "change.html", {"form": form, "title": "Reset Password"})
