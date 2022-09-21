from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe


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


def user_list(request):
    querySet = models.UserInfo.objects.all()

    return render(request, 'user_list.html', {"querySet": querySet})


# --------------------------------------------------------
class UserModleForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart_id"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}


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


def vipnumber(request):
    data_dict = {}
    value = request.GET.get("q","")
    if value:
        data_dict["mobile__contains"] = value


    # page
    page = int(request.GET.get("page",1))
    page_size = 3
    start = (page-1) * page_size
    end = page*page_size

    queryset = models.VipNumber.objects.filter(**data_dict).order_by("-level")[start:end]

    total_page = models.VipNumber.objects.filter(**data_dict).order_by("level").count()
    total_page_count, div = divmod(total_page,page_size)
    if div:
        total_page_count += 1

    # front 2 pages, after 2 pages
    plus = 2
    if page <= plus:
        start_page = 1
        end_page = 2*plus + 1

    elif page + plus > total_page_count:
        start_page = total_page_count - 2 * plus
        end_page = total_page_count
    else:
        start_page = page-plus
        end_page = page + plus

    page_list = []

    page_list.append('<li><a href="?page={}"><span class="glyphicon glyphicon-step-backward" aria-hidden="true"></span></a></li>'.format(1))

    if page > 1:
        page_list.append('<li><a href="?page={}"><span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span></a></li>'.format(page-1))
    else:
        page_list.append('<li><a href="?page={}"><span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span></a></li>'.format(1))

    for i in range(start_page,end_page + 1):
        if i == page:
            element = '<li class="active"><a href="?page={}">{}</a></li>'.format(i,i)
        else:
            element = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        page_list.append(element)

    if page < total_page_count:
        page_list.append('<li><a href="?page={}"><span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span></a></li>'.format(page+1))
    else:
        page_list.append('<li><a href="?page={}"><span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span></a></li>'.format(total_page_count))

    page_list.append('<li><a href="?page={}"><span class="glyphicon glyphicon-step-forward" aria-hidden="true"></span></a></li>'.format(total_page_count))
    page_string = mark_safe("".join(page_list))


    return render(request, "vipnumber.html", {"queryset": queryset,"value":value, "page_string":page_string})





class VipModelForm(forms.ModelForm):
    mobile = forms.CharField(
        label = "mobile",
        validators=[ RegexValidator(r'^1[3-9]\d{9}$', 'wrong number')])

    class Meta:
        model = models.VipNumber
        fields = ["mobile", "price", "level", "status"]
        # fields = "__all__"
        # exclude = ["mobile"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}

    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        exists = models.VipNumber.objects.filter(mobile=text_mobile).exists()

        if exists:
            raise ValidationError("The number already exists")
        return text_mobile


def vipnumber_add(request):
    if request.method == "GET":
        form = VipModelForm()
        return render(request, "vipnumber_add.html", {"form": form})

    form = VipModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/vip/number/list/")

    return render(request, "vipnumber_add.html", {"form": form})




class VipEditModelForm(forms.ModelForm):
    mobile = forms.CharField(
        label = "mobile",
        validators=[ RegexValidator(r'^1[3-9]\d{9}$', 'wrong number')])

    class Meta:
        model = models.VipNumber
        fields = "__all__"
        # exclude = ["mobile"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}

    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        print(self.instance.pk)
        exists = models.VipNumber.objects.exclude(id=self.instance.pk).filter(mobile=text_mobile).exists()

        if exists:
            raise ValidationError("The number already exists")
        return text_mobile


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