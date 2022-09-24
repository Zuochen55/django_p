from django.shortcuts import render,redirect
from app01.utils.bootstrap import BootstrapForm
from django import forms
from app01 import models

class LoginForm(BootstrapForm):
    name = forms.CharField(
        label="Username",
        widget=forms.TextInput
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )

def account_login(request):
    if request.method=="GET":
        form = LoginForm()
        return render(request,"login.html",{"form":form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        #print(form.cleaned_data)
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password","The username or password you entered was incorrect.")
            return render(request, "login.html", {"form": form})

        request.session["info"] = {"id": admin_object.id, "name": admin_object.name}
        return redirect("/admin/list/")


    return render(request, "login.html", {"form": form})