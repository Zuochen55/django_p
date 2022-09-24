from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class AdminModleForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput
    )
    class Meta:
        model = models.Admin
        fields = ["name", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control","placeholder":field.label}

    def clean_confirm_password(self):
        confirm = self.cleaned_data.get("confirm_password")
        pwd = self.cleaned_data.get("password")
        if confirm != pwd:
            raise ValidationError("The passwords don't match")
        return confirm

class AdminEditModleForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = ["name"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control","placeholder":field.label}

class AdminResetModleForm(forms.ModelForm):

    confirm_password = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput
     )
    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control","placeholder":field.label}

def clean_confirm_password(self):
    confirm = self.cleaned_data.get("confirm_password")
    pwd = self.cleaned_data.get("password")
    if confirm != pwd:
        raise ValidationError("The passwords don't match")
    return confirm

class UserModleForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart_id"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control","placeholder":field.label}

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
            field.widget.attrs = {"class": "form-control","placeholder":field.label}

    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        exists = models.VipNumber.objects.filter(mobile=text_mobile).exists()

        if exists:
            raise ValidationError("The number already exists")
        return text_mobile

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
            field.widget.attrs = {"class": "form-control","placeholder":field.label}

    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        print(self.instance.pk)
        exists = models.VipNumber.objects.exclude(id=self.instance.pk).filter(mobile=text_mobile).exists()

        if exists:
            raise ValidationError("The number already exists")
        return text_mobile