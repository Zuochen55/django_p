from django.shortcuts import render,redirect,HttpResponse
from app01.utils.bootstrap import BootstrapForm
from django import forms
from app01 import models
from app01.utils.code import check_code
from io import BytesIO

class LoginForm(BootstrapForm):
    name = forms.CharField(
        label="Username",
        widget=forms.TextInput
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(render_value=True)
    )
    code = forms.CharField(
        label="Verification Code",
        widget=forms.TextInput
    )

def account_login(request):
    if request.method=="GET":
        form = LoginForm()
        return render(request,"login.html",{"form":form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # Code
        user_input_code = form.cleaned_data.pop("code")

        code_session = request.session.get("image_code","")
        print(code_session)
        if code_session.upper() != user_input_code.upper():
            form.add_error("code","Wrong verification code!")
            return render(request, "login.html", {"form": form})


        # Password, Name
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password","The username or password you entered was incorrect.")
            return render(request, "login.html", {"form": form})

        request.session["info"] = {"id": admin_object.id, "name": admin_object.name}

        # session only 5 minutes
        request.session.set_expiry(60*60)

        return redirect("/admin/list/")


    return render(request, "login.html", {"form": form})

def image_code(request):
    img, code_string = check_code()

    request.session['image_code'] = code_string
    # 给session设置60秒超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())

def account_logout(request):
    request.session.clear()
    return redirect("/account/login/")